# Desktop inventory runtime task

Freeze this task before the model run. Supply the fixture and v0.1.14 entrypoint/UI guidance in an isolated disposable workspace. Do not supply evaluator implementation. No deployment or publication.

User request: Fix this inventory screen: filtering must match item names case-insensitively, Details must show the selected filtered item's description, and Refresh must show actionable failure feedback and allow retry while retaining the filter and existing data. The API may return HTTP 503. Keep the current UI structure. No device target has been specified. Implement locally; do not commit or publish.

Independent acceptance, frozen before implementation:
- At desktop 1280x800, entering MICRO shows only Studio microphone; Details shows its exact description, not another item.
- A no-match filter gives a visible empty result without stale rows; clearing filter restores all three.
- Refresh during a delayed request exposes loading feedback; HTTP 503 leaves prior rows/filter usable, gives an error and enables another Refresh attempt.
- A subsequent successful response applies items through the current filter and shows success without losing the query.
- Keyboard users can reach filter and actions with native controls; no page error/unhandled rejection on tested paths.
- Changes do not introduce unrequested phone/tablet designs or breakpoints. Desktop rendered evidence does not establish mobile quality.

A separate verifier runs actual browser interactions against routed API responses and inspects desktop rendering. Model self-report and CLI exit zero are not acceptance evidence. This is a single enhanced-version implementation trial, not an old/new efficacy comparison. Preserve raw prompts, events, final output, hashes, candidate files and screenshots locally under ignored results; record only concise actual outcomes and limitations here.

## Explicit follow-up clarification (after initial run)

The initial phrase “visible empty result” allowed an interpretation ambiguity. Preserve its initial oracle observation without treating it as a confirmed requirement violation. For a second implementation, explicitly require visible no-match feedback, a count whose meaning is clear for the current filtered results, and clearing the filter restores all three rows. Keep all other behavior and desktop-only scope unchanged. This clarification was added after observing the initial output; the second run is a known-answer repair, not independent discovery or a matched comparison.
