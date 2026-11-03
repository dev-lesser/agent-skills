> Historical upstream review with a separate current UI/UX import decision below. This personal adaptation excludes robotics and firmware skills.

# Upstream candidate review

This review selects reusable decision procedures, not the largest possible skill count. The historical upstream inventory
contained 41 procedures after adding domain modeling and Python type safety. The current personal catalog contains
39 procedures, including UI UX Pro Max; the historical counts below are not current catalog assertions. Project-specific
SDK/protocol commands, authority and build environments remain with their consuming repositories.

## Sources and review depth

| Source snapshot | Review performed | Limit |
| --- | --- | --- |
| [Matt Pocock](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2) | Inventory of 38 candidates: 27 shipped, seven in progress, four miscellaneous; candidate scope/overlap assessment | Not a full semantic audit of every supporting resource in all 38 directories |
| [Addy Osmani](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d) | All 25 frontmatters and leading procedure bodies checked for scope, triggers and overlap | Not a complete line-by-line audit of all reference files/scripts |
| [wshobson Python type safety](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/python-development/skills/python-type-safety) | Selected procedure/resources inspected for the Python bundle and compatibility/scope adaptation | Does not establish static-type-tool enforcement or runtime input validation |

These immutable references describe the inspected snapshots, not today's upstream state. Imported-file manifests retain
original/local hashes, licenses and narrow adaptations. A candidate inventory is not evidence that every candidate was
fully validated, imported or executed.

## Decisions

| Candidate group | Decision | Reason and application boundary |
| --- | --- | --- |
| Matt's existing `codebase-design` and `writing-for-agents` | Retain | Deep-module/interface and instruction-routing criteria already serve distinct tasks; do not replace their useful resources with summaries |
| Matt's [domain modeling](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling) | Add to common | Concrete domain vocabulary, state/ownership and invariants fill a useful design seam; trigger on actual domain modeling, not mandatory DDD layers for every feature |
| Matt's planning/interview/implementation/review workflows | No blanket import | Existing brainstorming, plans, TDD/SDD, review and debugging already own these decisions; imported workflows must not replace user authority or add approval rituals |
| Matt's issue-tracker/productivity/specialized or in-progress candidates | Defer | Optional external systems and task-specific workflows are not universal language scaffolding; no demonstrated gap requires another default procedure |
| Addy's existing deprecation/migration, observability and security | Retain | They cover distinct compatibility, diagnostic and trust-boundary tasks with project-scoped triggers |
| Addy's broader specification/planning/implementation/review/cleanup procedures | No additional import | Existing procedures cover the need; another author name does not justify duplicate invocation routes |
| Performance guidance | Conditional, not a universal gate | Start from a measured bottleneck and the actual runtime; do not profile or optimize every change by default |
| Python type safety | Add to Python only | Covers public annotations, protocols/generics and actual declared type checks without affecting Next-only projects or treating annotations as runtime validation |
| Additional configuration/style/runtime procedures | Defer unless a concrete gap appears | Existing ownership/configuration/naming/resource boundaries already cover common cases; review unsafe import-time configuration, secret handling or CSV examples before any later adoption |

The two additions keep their full procedure directories and needed resources, with narrow correctness/scope changes
recorded in provenance. New imported revisions have their own source records; an older source pin is not silently
rewritten to make unrelated imports appear upgraded. No new Addy procedure was needed after this comparison.

## Frontend and UI/UX candidates

On 2026-11-02, a targeted review compared widely used UI/UX resources with the five existing `react-ui` skills.
GitHub stars were used only to find candidates, not as evidence of skill quality, installation or model adherence.
The [frontend workflow guide](frontend-workflows.md) maps the retained procedures to design, critique, accessibility,
React performance and composition; the existing evaluations do not yet cover UI tasks.

| Inspected candidate | Decision | Reason and limit |
| --- | --- | --- |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/3a13158ff1f32156cbe144108de48eda2ecaed9a) | Defer | Design search/data overlaps existing guidance. Its Python search tooling and Claude plugin-root paths need host-specific compatibility and behavioral evaluation before an unmodified portable import. |
| [Microsoft Playwright CLI skill](https://github.com/microsoft/playwright-cli/tree/c2d8d199459d1480491bebf0a6b3587136b673fa) | Defer | Useful optional browser tooling, but it needs a CLI/browser runtime. A shared skill does not authorize installation, destructive browser actions or application execution. |
| Existing Anthropic frontend-design, Impeccable and Vercel UI skills | Retain | They already cover design direction, UI critique/polish, interface review, React performance and composition; Impeccable here is an instruction-only adaptation, not its upstream runtime. |

No new skill or runtime was imported from that historical comparison. The later scoped import decision below
supersedes the UI UX Pro Max deferral for its selected adapted payload only; it does not retroactively validate the
older candidate revision or establish model/UI effectiveness.

### Current scoped UI UX Pro Max import

The current addition pins [UI UX Pro Max at `713eef51b04efc98d6fa565323b495f7c9c89fd4`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/713eef51b04efc98d6fa565323b495f7c9c89fd4)
with its MIT evidence, complete selected search data, four standard-library runtime modules and two text references.
The adapted skill adds focused local design search to the existing five procedures, making six React UI skills.
Installers, hooks, host adapters and browser tooling remain excluded.

Use already available Python 3 only when execution is authorized; search is read-only by default and missing required
data is an error. A focused polish request does not authorize a replacement design system. Preserve the consuming
project's design/behavior and framework version; React 19 data does not establish React 18 compatibility. Persist
only a requested design record at a reviewed destination, with explicit overwrite authority for existing records.
Managed-path guards are preflight, not a concurrent-write sandbox. Source/hash/package and runtime regression checks
have their own evidence layers; neither search results nor static routing text proves fresh-session invocation,
rendered quality or interaction correctness. See [frontend workflows](frontend-workflows.md).

## Packaging and acceptance boundary

- Exactly one canonical owner per skill; bundles compose the same sources without combination-specific repositories.
- Keep task-triggered monorepo work in common and actual Rust-async guidance in Rust; neither requires an extra option.
- Full referenced resources and required license/NOTICE evidence travel in closed plugin payloads.
- Project commands/contracts/safety are consuming-repository lookups, not copied organization-specific assumptions.
- Frontmatter, hashes, links and package tests prove their own layer, not host installation or LLM compliance.

Public publication is not authorized by this review. Original-material licensing, secrets/proprietary scope and a real
release/host-refresh exercise remain separate decisions and checks. Further additions need a concrete missing use case,
non-overlapping trigger, preserved source evidence and a scoped validation plan—not an additive quota.
