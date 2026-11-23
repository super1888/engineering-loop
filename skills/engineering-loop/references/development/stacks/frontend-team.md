# Team frontend rules

**ID:** `dev.stack.frontend-team` · **Status:** partial. Extracted on 2026-11-21 from the team's React products, keeping rules that at least two products follow or that a check enforces. Three come from recorded incidents. The shared component and style catalog is still unavailable, and the open decisions at the end are not settled.

Use when the affected module is a React frontend. An existing project's effective instructions, design system and checks win where they differ. Read [React behavior checks](react.md) separately for a state or effect boundary. Baseline observed: React 19 with Vite or Next, TanStack Query 5; confirm the module's own versions first.

## Components and styles (F1)

- Take colours, radii and control heights from the theme or tokens. A hex literal, an inline `style` or a `dark ? …` branch in a page is the sign of a miss.
- One solid primary button per view or region.
- Build overlay triggers and close buttons from the shared Button. Never copy button CSS. Recorded incident: button appearance was written seven times and drifted.
- A pending button keeps its fill, shows a spinner and blocks clicks. Recorded incident: a pending primary lost its background and read as a clickable secondary.
- Every icon-only button has an accessible name, and status is never shown by colour alone.
- Animate only the project's allowed properties and never write `transition: all`. Under reduced motion, shorten animations instead of removing them.
- When asked only to move something, keep its existing font and media sizes.
- Settle a new visual direction with an approved mockup before writing its text specification. Recorded incident: an implementation that matched the first text specification was rejected on sight.

## antd 6 products

- Do not use props deprecated in v6 (a test enforces this in one product): `Spin.tip`, `Space.direction`, `Statistic.valueStyle`, `Alert.message`, `Drawer.width`, `Timeline.items[].children`.
- Where the product also uses Tailwind, wrap an antd component in a plain `div` to control grid, display or width. The antd root styles override layout utilities placed on the component.
- Upload with `Upload.Dragger`, `beforeUpload` returning false, and an explicit submit.

## Data and engineering (F2, F3, F5, F8)

- All HTTP goes through the product's single client. A page never builds a URL or calls `fetch` or axios.
- Keep IDs, cursors and version numbers as strings end to end, and show the public account number, not an internal identifier. See [R1](../rules/data-fidelity.md).
- Give each user submission one idempotency key, reuse it on retry and renew it after an edit. See [R4](../rules/async-idempotency.md).
- Never persist business data in browser storage.
- Paginate on the server and keep filter, sort, page and tab in the URL. Never fetch everything and filter in the browser.
- A wide table scrolls inside its own region. The page does not scroll horizontally and columns are not silently dropped.
- Generate API types from the contract and commit them first. Do not hand-edit them.

## Testing

- In Playwright use role or label locators, and read `getBoundingClientRect()` for a layout claim. Do not use `force`, fixed waits or `reuseExistingServer`. See [R9](../rules/rendered-ui.md).

## Adapted from public sources (unconfirmed for the team)

A team rule above wins where they differ, and every open decision below stays open. Component composition and data-loading rules are in the adapted section of [React behavior checks](react.md#adapted-from-public-sources-unconfirmed-for-the-team).

- Never remove a focus outline without a visible replacement on the same element, whichever outline style the product chose. A sticky header or footer must not cover the focused element.
- A flex child that truncates text needs `min-width: 0`. Without it the ellipsis never appears and the row overflows.
- Number columns, and figures compared down a column, use tabular numerals (`font-variant-numeric: tabular-nums`).
- A destructive action never runs on one click. It needs a confirmation or an undo window, in the product's own pattern.
- On a failed submit, show each error beside its field and move focus to the first one. Keep the submit button enabled until the request starts.
- Never block paste in an input.
- Format dates and numbers through the product's one formatter or `Intl`, not strings assembled in a page.

Optional antd lookup. A project may already have the Ant Design command-line tool (`antd`), which answers offline from bundled metadata. Where it is present, use it before writing antd 6 code:

- `antd info <Component> --version <installed version>` for the props that exist in that version, and `antd token <Component>` for its design tokens.
- `antd lint <changed files> --only deprecated` after the edit.

Do not install or upgrade it for this, and do not run its bug-report commands, which post to an external tracker. Without it, read the installed package's type definitions and the documentation for that version. Do not write antd props from memory.

## Enforcement

The strongest product enforces tokens with stylelint and architecture tests and runs Playwright with axe in CI; the others hold several rules as documentation only. Port the check together with the rule. Where a rule is documentation only in the current product, verify it in the rendered result.

## Open team decisions

The team's products differ on these. Follow the current product's choice and never introduce a second system into it. For a new product, raise the choice with its owner in stage 02.

- Component base: antd, Radix primitives with CSS Modules, or a mix with Tailwind. One product bans Tailwind, one does not use it and one mixes it with antd.
- Primary colour and danger pattern: the primary colour differs per product; a destructive action is a red button with an inline confirmation in two products and a normal button with a dialog in one.
- Forms: antd Form, React Hook Form with Zod, or hand-written.
- Request client and error shape: hand-written fetch with problem details, or a generated client with a code/data/message envelope.
- Client store: none beyond the query cache, or Zustand.
- Icon library: the antd icon set, or lucide.
- Target devices: desktop only, or desktop plus phone widths. See the [target-device gate](../../ui.md#frontend-design-gate-desktop-by-default).
- Focus outline and native scrollbars: always visible, or restyled.
- Copy: hard-coded Chinese, or an i18n catalog.
- Tooling: npm or pnpm; ESLint, Prettier and stylelint coverage.
