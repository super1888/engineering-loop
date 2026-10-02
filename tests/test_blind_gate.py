from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from blind_gate import gate, prepare, read_json, write_json


class BlindGateTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.suite = self.root / "suite.json"
        self.runs = self.root / "runs.json"
        self.packet = self.root / "reviewer/packet.json"
        self.key = self.root / "private/key.json"
        self.review = self.root / "reviewer/review.json"
        write_json(self.suite, {"id": "pilot", "cases": [{"id": "one", "task": "Write a requirement",
                   "criteria": [{"id": "boundary", "critical": True, "question": "Correct boundary?"}]}]})
        (self.root / "old.txt").write_bytes(b"old output\nline")
        (self.root / "new.txt").write_bytes(b"new output\nline")
        write_json(self.runs, {"suite": "pilot", "arms": {
            "baseline": {"one": {"artifact": "old.txt"}},
            "candidate": {"one": {"artifact": "new.txt"}}}})
        prepare(self.suite, self.runs, self.packet, self.key, seed=1)

    def submit(self, candidate: str, baseline: str, preference: str = "tie") -> dict:
        mapping = read_json(self.key)["mapping"]["one"]
        ratings = {side: {"boundary": candidate if mapping[side] == "candidate" else baseline}
                   for side in ("left", "right")}
        write_json(self.review, {"suite": "pilot", "reviewer": "test", "reviewer_kind": "human", "reviews": [
            {"id": "one", "ratings": ratings, "preference": preference, "reason": "Observed outcome"}]})
        return gate(self.suite, self.runs, self.packet, self.key, self.review)

    def test_blinded_packet_and_valid_candidate_pass(self):
        packet = self.packet.read_text(encoding="utf-8")
        self.assertNotIn("baseline", packet)
        self.assertNotIn("candidate", packet)
        self.assertEqual(self.submit("pass", "fail")["decision"], "pass")
        with self.assertRaisesRegex(ValueError, "Do not overwrite"):
            prepare(self.suite, self.runs, self.packet, self.key, seed=2)

    def test_critical_failure_and_baseline_preference_block(self):
        self.assertEqual(self.submit("fail", "pass")["decision"], "fail")
        baseline_side = next(side for side, arm in read_json(self.key)["mapping"]["one"].items()
                             if side in ("left", "right") and arm == "baseline")
        self.assertEqual(self.submit("pass", "pass", baseline_side)["decision"], "fail")

    def test_artifact_mutation_invalidates_review(self):
        self.submit("pass", "pass")
        (self.root / "new.txt").write_text("changed after review", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Artifact changed"):
            gate(self.suite, self.runs, self.packet, self.key, self.review)

    def test_line_ending_conversion_keeps_same_review(self):
        self.submit("pass", "pass")
        (self.root / "new.txt").write_bytes(b"new output\r\nline")
        self.assertEqual(gate(self.suite, self.runs, self.packet, self.key, self.review)["decision"], "pass")

    def test_rubric_mutation_invalidates_review(self):
        self.submit("pass", "pass")
        suite = read_json(self.suite)
        suite["cases"][0]["criteria"][0]["critical"] = False
        write_json(self.suite, suite)
        with self.assertRaisesRegex(ValueError, "Golden suite changed"):
            gate(self.suite, self.runs, self.packet, self.key, self.review)

    def test_packet_mutation_invalidates_review(self):
        self.submit("pass", "pass")
        packet = read_json(self.packet)
        packet["cases"][0]["left"] = "edited after review"
        write_json(self.packet, packet)
        with self.assertRaisesRegex(ValueError, "Review packet changed"):
            gate(self.suite, self.runs, self.packet, self.key, self.review)

    def test_fixture_context_mutation_invalidates_review(self):
        fixture = self.root / "fixture"
        fixture.mkdir()
        brief = fixture / "BRIEF.md"
        brief.write_bytes(b"Accepted task context\n")
        suite = read_json(self.suite)
        suite["cases"][0]["fixture"] = "fixture"
        write_json(self.suite, suite)
        packet = self.root / "fixture-reviewer/packet.json"
        key = self.root / "fixture-private/key.json"
        prepare(self.suite, self.runs, packet, key, seed=1)
        self.packet, self.key = packet, key
        self.submit("pass", "pass")
        brief.write_bytes(b"Accepted task context\r\n")
        self.assertEqual(gate(self.suite, self.runs, packet, key, self.review)["decision"], "pass")
        brief.write_bytes(b"Changed task context\n")
        with self.assertRaisesRegex(ValueError, "case context changed"):
            gate(self.suite, self.runs, packet, key, self.review)

    def test_private_mapping_cannot_be_nested_under_review_directory(self):
        packet = self.root / "reviewer/another-packet.json"
        key = self.root / "reviewer/private/key.json"
        with self.assertRaisesRegex(ValueError, "outside the review-packet directory"):
            prepare(self.suite, self.runs, packet, key, seed=1)
        self.assertFalse(packet.exists())
        self.assertFalse(key.exists())

    def test_gate_rejects_private_mapping_inside_review_directory(self):
        self.submit("pass", "pass")
        key = self.root / "reviewer/private/key.json"
        write_json(key, read_json(self.key))
        with self.assertRaisesRegex(ValueError, "outside the review-packet directory"):
            gate(self.suite, self.runs, self.packet, key, self.review)

    def test_model_review_can_pass_pilot_but_not_release(self):
        self.submit("pass", "pass")
        review = read_json(self.review)
        review["reviewer_kind"] = "model"
        write_json(self.review, review)
        self.assertEqual(gate(self.suite, self.runs, self.packet, self.key, self.review,
                              require_human=False)["decision"], "pass")
        release = gate(self.suite, self.runs, self.packet, self.key, self.review)
        self.assertEqual(release["decision"], "fail")
        self.assertIn("Human blinded review required for release", release["reasons"])


if __name__ == "__main__":
    unittest.main()
