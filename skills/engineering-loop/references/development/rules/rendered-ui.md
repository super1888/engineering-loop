# R9 Rendered behavior and accessibility evidence

**ID:** `dev.risk.rendered-ui` · **Status:** available UI and verification pointers.

**Trigger:** A claim concerns visible layout, responsive behavior, focus/navigation, user feedback or accessibility. Match the evidence to the actual claim and target rather than treating source tokens as rendered behavior.

Read the relevant [UI guidance](../../ui.md), including its [target-device gate](../../ui.md#frontend-design-gate-desktop-by-default). For visual/responsive defects apply [Rendered visual and responsive defects](../../verification-boundaries.md#rendered-visual-and-responsive-defects); for accessibility/status claims apply [Accessibility scans and status feedback](../../verification-boundaries.md#accessibility-scans-and-status-feedback). Read only the applicable detailed sections; those sources retain their full constraints.

**Nearby exception:** A nonvisual metadata-only change needs no unrelated rendering/language matrix. A settled copy or spacing edit needs its affected checks, not a redesign workshop; existing required device behavior remains effective.

**Verification:** Record the affected route, target, content/state, artifact and observed result through the existing UI/acceptance record. Missing rendering or interaction evidence remains unverified. A local design preference does not authorize unrelated interface redesign.
