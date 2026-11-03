# Frontend design, review and interaction guidance

Use this guide to select existing `react-ui` skills, not as a required workflow or a replacement for a project's
design system, accessibility requirements, package instructions or the user's request. The bundle contains reviewed
upstream skill material; its source, adaptations, licenses and pinned revisions remain in
[`provenance/skill-sources.json`](../provenance/skill-sources.json).

## Choose by the requested work

| Request | Skill | Boundary |
| --- | --- | --- |
| Create or substantially reshape a UI; avoid a generic look | [`frontend-design`](../plugins/react-ui/skills/frontend-design/SKILL.md) | Start from the actual brief, audience and existing visual language. Upstream's fictional client scenario is not evidence about the current user. |
| Audit, critique, polish or harden a specific existing UI | [`impeccable`](../plugins/react-ui/skills/impeccable/SKILL.md) | Select the relevant instruction-only reference; preserve existing design and behavior unless redesign is requested. The upstream CLI, detector, hooks and browser tooling are not included. |
| Find local styles, palettes, typography, charts or UX/stack guidance for a visual task | [`ui-ux-pro-max`](../plugins/react-ui/skills/ui-ux-pro-max/SKILL.md) | Use focused search within the existing design; a new design system needs a task that requests that direction. Python search is optional, not permission to install a runtime. |
| Review a target for interface and accessibility issues | [`web-design-guidelines`](../plugins/react-ui/skills/web-design-guidelines/SKILL.md) | Use the pinned local checklist and report findings with locations and evidence. Interpret rules against the actual control and project. |
| Examine React/Next.js rendering, data or bundle performance | [`vercel-react-best-practices`](../plugins/react-ui/skills/vercel-react-best-practices/SKILL.md) | Apply relevant guidance to the installed framework and measured problem; a rule or build alone does not establish a performance gain. |
| Change a React component's composition, state ownership or reusable API | [`vercel-composition-patterns`](../plugins/react-ui/skills/vercel-composition-patterns/SKILL.md) | Use composition where the existing component and callers benefit; do not add compound components or context by default. |

UI-specific anti-slop guidance is already present in `frontend-design` and `impeccable`; neither provides an
automatic detector in this bundle. Treat visual tropes as prompts for review, not a universal ban on fonts,
colors, cards, layouts or motion. Avoid inventing product facts or replacing a requested or established design
merely because it resembles a template. There is no separately owned `ai-slop` skill in this catalog.

These skill identities make selection possible; they do not prove a host discovered or invoked them, that an agent
followed them, or that a UI improved. Do not install or enable additional tools merely to use the guidance.

## Local UI/UX search without a new design workflow

`react-ui` has six skills. UI UX Pro Max adds local search data, four Python standard-library modules and two text
references from the pinned MIT source. It does not add upstream installers, hooks, host adapters or browser tooling.
Use it alongside the applicable design/review procedure; it complements rather than replaces existing routing.

- **Scope:** for focused polish, search the relevant concern within the approved design, tokens, components and
  behavior. Do not generate a replacement system for an existing screen unless the request covers redesign.
- **Runtime:** run the skill-local search only when execution is authorized and Python 3.9+ already exists. Resolve the
  directory containing the actually loaded skill, including cache installations; use Python's `-B` option to avoid
  bytecode writes. Search is read-only by default. Missing Python is a limitation, not installation authorization.
- **Framework:** detect the installed stack and version; inspect applicability/status in returned guidance. React data
  targets React 19, so a React 18 result can contain deprecation advice rather than compatible implementation
  guidance. Use version-appropriate project references or stack-neutral UX guidance; never migrate to fit a result.
- **Failures:** missing/unreadable required data aborts search and persistence. Zero matches or defaulted reasoning
  are not verified database recommendations. Inspect JSON source identities/reasoning status before recommending a
  new system; disclose unresolved matches and never persist an unverified fallback.
- **Writes:** persist only for a requested design record at an explicitly reviewed project destination after reading
  existing records. Preserve current records; overwrite requires separate explicit authority. Managed child symlinks
  are rejected, but the selected root may resolve through a link. These guards are preflight, not a sandbox against
  concurrent filesystem changes.

The complete [skill procedure](../plugins/react-ui/skills/ui-ux-pro-max/SKILL.md) owns search and persistence commands;
this guide does not duplicate a second command reference. Search results remain recommendations, not authority to
change project behavior, factual content, telemetry density, framework versions or safety confirmations. A search
pass is not evidence of rendered quality, accessibility conformance or interaction correctness.

## Evidence for the changed surface

- **Source or supplied image only:** inspect the relevant implementation or provided design and report the findings
  at that layer. An image cannot establish clickable area, keyboard behavior, accessibility-tree output or runtime
  state; source alone does not establish rendered layout.
- **Visual review, when in scope and execution is authorized:** inspect the actual viewport and relevant loading,
  empty, error, populated and responsive states. Record the target, viewport and what was observed; a screenshot
  from another state or viewport is not proof of this one.
- **Interaction, when in scope and execution is authorized:** use pointer and keyboard to verify the requested
  action, including focus visibility, activation and the intended clickable area. A native button or link already
  provides keyboard behavior; do not add redundant key handlers solely to satisfy a static pattern.
- **Accessibility:** assess applicable requirements, states and exceptions for the actual interface. Useful W3C
  references include [keyboard](https://www.w3.org/TR/WCAG22/#keyboard), [focus visible](https://www.w3.org/TR/WCAG22/#focus-visible),
  [text contrast](https://www.w3.org/TR/WCAG22/#contrast-minimum) and [target size](https://www.w3.org/TR/WCAG22/#target-size-minimum).
  A checklist, screenshot or automated scan alone is not a WCAG conformance certification or proof of usability.

Read-only review does not authorize edits. When execution is excluded, use supplied evidence and state what remains
unverified; do not require a browser, service, `DESIGN.md`, MCP server or dependency installation. If execution is
allowed, use the project's existing tools and do not treat guidance as permission to deploy or access hardware.

## Upstream references

These links document the pinned origins, not additional installed components or a claim of measured improvement:

- [Anthropic frontend-design at the pinned revision](https://raw.githubusercontent.com/anthropics/claude-plugins-official/465f09344424225c25d438f2e052732c3d688d2f/plugins/frontend-design/skills/frontend-design/SKILL.md)
- [Impeccable at the pinned revision](https://github.com/pbakaus/impeccable/tree/936867543ac2576920d663cc9803597f6044f3ac) — this repository packages only the selected instruction-only adaptation described above.
- [Vercel agent skills at the pinned revision](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278)
- [Vercel Web Interface Guidelines at the pinned revision](https://github.com/vercel-labs/web-interface-guidelines/blob/434b7f91364665f2f733b310ec54809bf8f37937/command.md)
- [UI UX Pro Max at the pinned revision](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/713eef51b04efc98d6fa565323b495f7c9c89fd4) — selected data/runtime/references only, with recorded local adaptations.
