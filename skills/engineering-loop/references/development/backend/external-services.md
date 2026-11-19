# B7 External service and SDK changes

**ID:** `dev.backend.external-services` · **Status:** available execution baseline; provider adapters, package/version choices and commercial policy remain project bindings.

## Scope and inputs

Use for adapters, provider requests/callbacks, protocol errors or SDK transport changes. Identify the maintained provider contract, actual consuming adapter/version, credential source, required capability combination and existing test boundary. A successful generic connection does not prove every requested operation.

## Execute

1. Trace request construction, serialization, authentication, actual transport, response mapping and effects. Reuse the project's adapter/credential boundary; do not move privileged credentials into a client or invent endpoint paths.
2. Map accepted inputs/errors and known provider outcomes to the current contract. Keep unsupported capability, malformed request and temporary unavailability distinct where they produce different accepted behavior.
3. Apply [R8](../rules/sdk-transport.md) when dependency replacement can affect transport and [R4](../rules/async-idempotency.md) when callbacks/retries/unknown outcomes can repeat work.
4. Preserve identity, resource access and required recovery through [R2](../rules/access.md) when affected. Do not weaken authentication, expose secrets or silently change business fallback policy to obtain a successful call.
5. Select a controlled protocol/loopback fixture where it proves the changed boundary. Actual provider calls or external effects require their existing authority and configured environment; the route itself does not grant them.

## Verify

- Exercise the affected request/response/error mapping against independently accepted examples, preserving the ordinary successful case.
- For SDK dependency/transport changes, test the real affected SDK path with its resulting dependencies; serialization or mocked clients alone are insufficient.
- For a capability combination, test that actual combination only when required. Distinguish local transport, provider acceptance, parsed structure and task semantics using [verification](../../verification.md).

## Deliver and bind

Record adapter/dependency identity, contract source, actual fixture/provider scope, relevant outcomes and remaining limits using [delivery evidence](../delivery.md). Provider-specific packages, callbacks, retries, costs and capability policies remain with their maintained project sources.
