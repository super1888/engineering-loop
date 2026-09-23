"""Prepare blinded paired reviews and gate a candidate against a fixed golden suite."""

import argparse
import hashlib
import json
from pathlib import Path
import random


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def file_digest(path: Path) -> str:
    return digest(normalized(path.read_bytes()))


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def artifact(runs_path: Path, entry: dict) -> tuple[str, str]:
    path = (runs_path.parent / entry["artifact"]).resolve()
    content = normalized(path.read_bytes())
    return content.decode("utf-8"), digest(content)


def validate_suite(suite: dict, runs: dict) -> None:
    cases = suite["cases"]
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)) or not ids:
        raise ValueError("Golden case IDs must be unique and nonempty")
    for case in cases:
        criteria = [item["id"] for item in case["criteria"]]
        if len(criteria) != len(set(criteria)) or not criteria:
            raise ValueError(f"Invalid criteria for {case['id']}")
    if runs["suite"] != suite["id"] or set(runs["arms"]) != {"baseline", "candidate"}:
        raise ValueError("Run arms or suite do not match the golden suite")
    for arm in runs["arms"].values():
        if set(arm) != set(ids):
            raise ValueError("Every arm must include every golden case exactly once")


def prepare(suite_path: Path, runs_path: Path, packet_path: Path, key_path: Path,
            seed: int | None = None) -> None:
    if packet_path.resolve() == key_path.resolve() or packet_path.resolve().parent == key_path.resolve().parent:
        raise ValueError("Keep the private key outside the review-packet directory")
    if packet_path.exists() or key_path.exists():
        raise ValueError("Do not overwrite a frozen review packet or private mapping")
    suite, runs = read_json(suite_path), read_json(runs_path)
    validate_suite(suite, runs)
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    packets, mapping = [], {}
    for case in suite["cases"]:
        case_id = case["id"]
        left_arm = rng.choice(("baseline", "candidate"))
        right_arm = "candidate" if left_arm == "baseline" else "baseline"
        left, left_hash = artifact(runs_path, runs["arms"][left_arm][case_id])
        right, right_hash = artifact(runs_path, runs["arms"][right_arm][case_id])
        context = ((suite_path.parent / case["fixture"] / "BRIEF.md").read_text(encoding="utf-8")
                   if "fixture" in case else case.get("context", ""))
        packets.append({"id": case_id, "task": case["task"], "context": context,
                        "criteria": case["criteria"],
                        "left": left, "right": right})
        mapping[case_id] = {"left": left_arm, "right": right_arm,
                            "hashes": {left_arm: left_hash, right_arm: right_hash}}
    packet = {"suite": suite["id"], "cases": packets}
    write_json(packet_path, packet)
    write_json(key_path, {"suite": suite["id"], "suite_sha256": file_digest(suite_path),
                          "packet_sha256": file_digest(packet_path),
                          "mapping": mapping})


def gate(suite_path: Path, runs_path: Path, packet_path: Path, key_path: Path,
         review_path: Path, require_human: bool = True) -> dict:
    suite, runs = read_json(suite_path), read_json(runs_path)
    validate_suite(suite, runs)
    key, packet, review = read_json(key_path), read_json(packet_path), read_json(review_path)
    if key["suite"] != suite["id"] or review["suite"] != suite["id"] or packet["suite"] != suite["id"]:
        raise ValueError("Suite mismatch")
    if file_digest(suite_path) != key["suite_sha256"]:
        raise ValueError("Golden suite changed after blinding")
    if file_digest(packet_path) != key["packet_sha256"]:
        raise ValueError("Review packet changed after blinding")
    expected_ids = {case["id"] for case in suite["cases"]}
    if (set(key["mapping"]) != expected_ids or len(packet["cases"]) != len(expected_ids)
            or {case["id"] for case in packet["cases"]} != expected_ids):
        raise ValueError("Incomplete packet or private mapping")
    packet_by_id = {case["id"]: case for case in packet["cases"]}
    reviews = review["reviews"]
    if len(reviews) != len(expected_ids) or {item["id"] for item in reviews} != expected_ids:
        raise ValueError("Review must cover every case exactly once")
    by_id = {item["id"]: item for item in reviews}
    failures = []
    if review.get("reviewer_kind") not in {"human", "model"}:
        raise ValueError("Review must declare reviewer_kind as human or model")
    if require_human and review["reviewer_kind"] != "human":
        failures.append("Human blinded review required for release")
    for case in suite["cases"]:
        case_id = case["id"]
        mapping = key["mapping"][case_id]
        if set((mapping["left"], mapping["right"])) != {"baseline", "candidate"}:
            raise ValueError(f"Invalid arm mapping: {case_id}")
        for side in ("left", "right"):
            if digest(normalized(packet_by_id[case_id][side].encode("utf-8"))) != mapping["hashes"][mapping[side]]:
                raise ValueError(f"Packet does not match blinded artifact: {case_id}/{side}")
        for arm in ("baseline", "candidate"):
            _, current_hash = artifact(runs_path, runs["arms"][arm][case_id])
            if current_hash != mapping["hashes"][arm]:
                raise ValueError(f"Artifact changed after blinding: {case_id}/{arm}")
        item = by_id[case_id]
        ratings = item["ratings"]
        expected_criteria = {criterion["id"] for criterion in case["criteria"]}
        if set(ratings) != {"left", "right"} or any(set(ratings[side]) != expected_criteria for side in ratings):
            raise ValueError(f"Incomplete rubric: {case_id}")
        if item["preference"] not in {"left", "right", "tie", "uncertain"} or not item.get("reason", "").strip():
            raise ValueError(f"Missing review decision or reason: {case_id}")
        candidate_side = "left" if mapping["left"] == "candidate" else "right"
        baseline_side = "right" if candidate_side == "left" else "left"
        for criterion in case["criteria"]:
            name = criterion["id"]
            candidate = ratings[candidate_side][name]
            baseline = ratings[baseline_side][name]
            if candidate not in {"pass", "fail", "uncertain"} or baseline not in {"pass", "fail", "uncertain"}:
                raise ValueError(f"Invalid rating: {case_id}/{name}")
            if candidate == "uncertain":
                failures.append(f"{case_id}/{name}: candidate result uncertain")
            elif criterion["critical"] and candidate != "pass":
                failures.append(f"{case_id}/{name}: critical check failed")
            elif baseline == "pass" and candidate == "fail":
                failures.append(f"{case_id}/{name}: regression against baseline")
        if item["preference"] == baseline_side:
            failures.append(f"{case_id}: blinded reviewer preferred baseline")
        elif item["preference"] == "uncertain":
            failures.append(f"{case_id}: blinded preference uncertain")
    return {"suite": suite["id"], "profile": "release" if require_human else "pilot",
            "decision": "fail" if failures else "pass",
            "case_count": len(expected_ids), "reasons": failures,
            "reviewer": review.get("reviewer", "unspecified"),
            "reviewer_kind": review["reviewer_kind"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "gate"):
        command = sub.add_parser(name)
        for option in ("suite", "runs", "packet", "key"):
            command.add_argument(f"--{option}", type=Path, required=True)
        if name == "prepare":
            command.add_argument("--seed", type=int, help="Only for deterministic tests")
        else:
            command.add_argument("--review", type=Path, required=True)
            command.add_argument("--output", type=Path, required=True)
            command.add_argument("--pilot", action="store_true", help="Allow model-only review for exploration")
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            prepare(args.suite, args.runs, args.packet, args.key, args.seed)
        else:
            result = gate(args.suite, args.runs, args.packet, args.key, args.review,
                          require_human=not args.pilot)
            write_json(args.output, result)
            print(result["decision"], "; ".join(result["reasons"]))
            if result["decision"] != "pass":
                raise SystemExit(1)
    except (KeyError, ValueError, OSError, UnicodeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
