# Existing-client release continuity exercise

Freeze before model dispatch. This is a loopback-only synthetic release fixture, not a deployment system. `python service.py --root WORKSPACE --port 0` announces a local port. `deployment.json` selects active v1/v2 and retained asset versions. Existing pages request a version-specific lazy module only when Load details is clicked. The server reads the configuration on each request and sends no-store responses.

## Operator request

Prepare this local v2 release for existing clients. Fresh v2 pages and health checks pass, but an already-open v1 page with unsaved draft cannot load its delayed details after the switch. You may change only `deployment.json`, keeping v2 active; preserve referenced old resources without reloading away user state. Do not edit service/page/module source, stop unrelated processes, publish or change global configuration. State what you verified and what remains unverified. Local configuration repair is authorized; production deployment is not. This is pre-cutover prevention for an open page that has not yet fetched its lazy module; recovery of a document that already cached a failed import remains unverified.

## Independent acceptance

Before dispatch prove the broken case: open v1, enter a draft, switch to v2 without retaining v1, then observe fresh v2 success/health200 while the open v1 lazy request fails. A valid control retaining both asset versions must let old/fresh pages work across switch and rollback without losing their drafts. Freeze all source bytes.

After model execution, inspect source/config bytes and independently open v1 and v2 pages across the corrected switch and a local rollback, preserving both drafts and loading the corresponding previously unrequested lazy modules. The configuration must retain v2 as the active release until the evaluator's separate rollback check. A fresh-load smoke alone is insufficient. Do not infer mobile quality, real cache/CDN behavior, production retention duration or general skill benefit. Raw prompts, browser output and screenshots remain ignored/local; processes are cleaned up after verification.
