# Match shared component and style templates

Use only for an actual component/style reuse need in stage 02 design or stage 03 frontend implementation. Keep that stage's authority and [UI target-device gate](../ui.md#frontend-design-gate-desktop-by-default). A template cannot introduce a business action, mobile scope, package installation or implementation authority by itself.

## Catalog status

Status: **pending**. [Frontend-Design-Common](https://github.com/super1888/Frontend-Design-Common) is the intended external team source. The connected repository read on 2026-11-19 returned an empty repository, so no template body, release or package binding was available. Recheck the actual source when content is supplied; the slots below remain unfilled. Do not claim that ten buttons or any particular template has been loaded.

Maintained catalog reference/version:

<!-- Reserved for the accepted catalog's actual location and version. Keep private bindings local. -->

Approved template entries:

<!-- Reserved for real entries conforming to the contract below; do not invent sample IDs as live templates. -->

## Match and read

1. Reuse the project's effective design system and accepted component choices. If an explicit template ID/reference is supplied, resolve that actual identity first; unknown identity or incompatibility is a gap to reconcile, not permission to silently choose another.
2. Otherwise use catalog metadata and aliases to find candidates. Filter against the affected framework/component library/version, allowed dependencies, intended action/meaning, required states and accepted target. A name or visual resemblance is not a compatibility check.
3. Apply accepted tokens and visual preferences among compatible candidates. Investigate project precedent first. Choose low-impact reversible details within existing authority; ask only an unresolved distinction that materially changes acceptance or costly rework. Do not ask the user to choose internal skill routes.
4. Read the selected template's actual parameters, state variants, examples and dependency instructions. Read a related template only when the current composition needs it; do not preload the complete collection.
5. If no catalog/candidate is available, use a suitable existing project component within the accepted scope. Preserve an explicit template requirement: when it or another necessary constraint cannot be satisfied, report the precise gap and pause dependent work. Optional missing templates do not block an otherwise established local fix.

## Entry contract

| Field | Meaning |
|---|---|
| Stable ID, aliases, status | Exact identity; discovery terms; available/partial/pending/retired |
| Purpose and exclusions | User action, intended contexts and legitimate cases where it must not apply |
| Compatibility | Supported framework/library/version, actual dependencies and target constraints |
| Parameters and states | Accepted inputs/defaults, loading/disabled/error/focus variants where applicable |
| Tokens and composition | Inherited design tokens, allowed variations and required related components |
| Source and example | Actual body/example location, maintained version and responsible source |
| Verification | Representative rendering/interaction and compatibility checks, with a nearby counterexample |

These fields do not make a pending entry usable. Keep detailed component usage and examples in the owning catalog; the coordinator indexes it and retains integrated acceptance. Track PMS work by deliverable rather than one card per button.
