# Review a change for security defects

**Challenge focus:** Which untrusted input reaches which sensitive operation through the changed code, and what stops it today?

Use with [review.md](review.md) when a change touches authentication, authorization, secrets, input parsing, command or query construction, deserialization, or data crossing a trust boundary. Decide that by what the change touches, not its size: a two-line edit to a permission check qualifies, a large rename does not. This covers defects the change introduces. It is not a repository audit, threat model or dependency scan, and it stays read-only.

## Method

1. **Learn the local pattern first.** Find how the repository already validates input, checks permissions, builds queries and handles secrets in comparable code. A departure from an established safeguard, or a removed check with no replacement, is the strongest lead.
2. **Find candidates.** Follow data from each entry point the change adds or alters to the sensitive operation it reaches: query, command, file path, template, deserializer, outbound request, privilege decision, log or response.
3. **Filter each candidate separately.** Restate the claim precisely: who the attacker is and what they can already do, which input they control, the path to the operation and the resulting harm. Then look for what defeats it: validation in callers, a framework default, an earlier guard. Where the host provides an independent reviewer and the checkpoint warrants one, give it the candidate and the code without the finder's reasoning; otherwise make this a separate pass and say no independent check was made.
4. **Report only what survives** with a shown path and real impact. Give dropped candidates as a count; keep an unsettled one as a named open question only when the harm would be severe.

## Do not report by default

Unless the project's requirements put them in scope:

- Denial of service, resource exhaustion and missing rate limits.
- Absent hardening or defense in depth with no concrete exploit path.
- Outdated dependencies; they belong to the project's dependency process.
- Code that runs only in tests, and documentation.
- Races or timing issues without a practical trigger.
- Missing validation on a field with no shown security consequence.
- Missing audit logging, or ordinary non-sensitive values written to logs.

## Trust assumptions

State those relied on. Project policy overrides these defaults.

- Environment variables, command-line flags and deployment configuration belong to the operator, not the attacker.
- Client-side code is untrusted and need not enforce permissions; the server must.
- A long random identifier is not guessable, but holding one is not authorization.
- A framework's default output escaping holds unless the change uses its raw-output path.
- Secrets or personal data in logs are a finding; ordinary identifiers are not.

## Report

For each finding give location, the attacker's starting position, the path, the impact, a severity set by that impact, and the existing pattern it departs from. Use the project's defect record or the acceptance record's existing fields. State what was not examined. No findings means none were shown in this diff, not that the change is secure.
