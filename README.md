# DevLesserAgentSkills

One versioned source for reusable engineering skills and **optional** advisory hooks. Language and
framework bundles are folders in this repository, not separate repositories and not one repository per combination.

This personal repository contains plugin-owned canonical skills, prepared installable bundles, tooling, and provenance.
It excludes robotics and firmware bundles. Imported material retains its recorded source revisions and individual notices;
historical upstream releases and evaluations are not evidence for this repository.

## Quick start

Clone and review this repository, register its marketplace, and install the bundles your project needs:

```bash
git clone https://github.com/dev-lesser/agent-skills.git
codex plugin marketplace add ./agent-skills
codex plugin add common@dev-lesser-agent-skills
codex plugin add python@dev-lesser-agent-skills
codex plugin list --marketplace dev-lesser-agent-skills
```

Choose other bundles from the table below. Inspect installed versions and start a fresh session before checking
skill discovery. Installation and listing do not establish invocation or model adherence. The checkout must remain
available for a local marketplace; see [host setup](docs/hosts.md) for Git sources and refresh boundaries.

## First-run recovery: plugin not found

If Codex reports `plugin X not found in marketplace dev-lesser-agent-skills`, first check whether the reviewed source
has been registered on this host. If not, register it **once**:

```bash
codex plugin marketplace add /path/to/agent-skills
```

Or, from this `agent-skills` checkout:

```bash
codex plugin marketplace add .
```

Then retry the selected adds. If that marketplace name is already
registered, inspect its source/revision instead of automatically retargeting it: Codex can reuse a stale same-name Git
cache. Changed URL/ref settings alone do not attest installed bytes. See [host setup](docs/hosts.md).

## Ownership boundaries

| Component | Owns |
| --- | --- |
| `agent-skills` | Reusable skill bodies/resources, source licenses, plugin bundles, opt-in advisory hook |
| Consuming project | Actual commands, native manifests, domain contracts, project-local rules and safety decisions |
| Agent host | Download/cache, explicit activation, trust, authentication, refresh and session discovery |

Shared skill bodies stay with the provider and host cache. Each developer or CI host needs its own reviewed source
registration, installation and refresh. A host refresh does not remove or overwrite project-local customizations.

## Structure

```text
catalog.json                       # Stable bundle/skill ownership, release version and composition
plugins/<bundle>/skills/<skill>/   # Canonical complete procedures/resources; edit these
provenance/skill-sources.json      # v2 ledger: root-relative canonical owners, pins and reviewed hashes
plugins/<owner>/references/       # Canonical shared references; other bundle copies are generated
plugins/<owner>/licenses/         # Canonical imported notices; other bundle copies are generated
plugins/common/exports/codex/agents/*.toml # Four canonical model-free generic roles
plugins/common/agents/*.md         # Generated Claude role adapters
plugins/session-guidance/hooks/session-start.sh # Canonical opt-in printf-only advisory
LICENSE, LICENSING.md              # Canonical legal policy; plugin-root copies are generated
scripts/build_plugins.py           # Stdlib release preparation and --check; never consumer installation
.agents/plugins/marketplace.json   # Generated Codex marketplace index
.claude-plugin/marketplace.json    # Generated Claude marketplace index
```

Each `plugins/<bundle>/` is both its canonical authoring home and a closed installable package. Its generated
metadata, role adapters and destination reference/license copies are not separately maintained sources. Use the
ledger to find a shared resource's owner before editing. The retired `source/` tree and root hook mirror are absent.
The root `.agents/plugins/` is the marketplace index; project-local `.agents/skills/` is a separate host discovery
mechanism, not a required shared-skill copy. Each plugin's root `plugin.json` is the portable format, with a generated
`.claude-plugin/plugin.json` adapter.

Preparation preserves complete canonical procedure bytes, resolves declared shared resources from their owners,
rewrites only destination-copy links and prepares generated metadata. It validates frontmatter, reviewed hashes,
local resource closure and managed paths; unknown outward references fail rather than disappearing. It never
replaces the whole plugin tree or approves a changed canonical hash. The builder updates changed generated files
with rollback on a caught failure; this is not a crash-atomic release. See [provenance](docs/provenance.md).

Imported procedures and shared references may retain specific examples or assumptions. Review them against the
actual consuming project. Static checks do not establish discovery, invocation, adherence or UI effectiveness.

## Choose a project, not a list of skills

Select the smallest relevant bundle set from this repository's catalog. Composition metadata does not auto-install dependencies.

| Project | Bundle selection |
| --- | --- |
| General Python and automation | `common`, `python` |
| FastAPI / Litestar API | `common`, `python`, `api-contracts`, `fastapi` / `litestar` |
| React + Vite frontend | `common`, `typescript`, `react-ui` |
| NestJS backend | `common`, `typescript`, `api-contracts`, `nestjs` |
| Next.js full stack | `common`, `typescript`, `react-ui`, `api-contracts`, `nextjs` |
| Rust | `common`, `rust`; async guidance applies only to actual async tasks |
| Python API + React / Next.js monorepo | Union of those selections; common cross-package guidance is task-triggered |
| Any project requesting a session reminder | Separately opt in to `session-guidance` and review hook trust |

REST/API contracts are shared, not FastAPI-specific: both FastAPI and Litestar select `api-contracts` plus their
respective framework bundle. Framework skills implement the same wire-contract principles through their own routing,
DI, errors and test APIs. The API-design skill's Python REST asset is an illustrative FastAPI example, not a Litestar
scaffold or a reason to install FastAPI in another framework.

A single Next.js project gets no dedicated Python bundle. In a mixed-language monorepo the host has the union, while
project package routing chooses the relevant instructions for the actual task. Skill metadata can still be visible;
this is not a per-directory model sandbox. Common principles may use another language as an example without adopting
that language, runtime or dependency.

There are **11 bundles and 39 skills**. `session-guidance` has no skills and is never selected automatically.
Monorepo change guidance lives in Common; Rust async guidance lives in Rust. These are task conditions, not more setup options.
React UI contains six skills, including `ui-ux-pro-max` for scoped local design-data search. Use focused searches for
polish within an existing design; request a new design system only when the task calls for one. Preserve project
behavior, design tokens and framework versions. See [frontend workflows](docs/frontend-workflows.md) for execution,
persistence and React-version limits. The consumer project owns its setup and decisions.

## Shared methods, project-local contracts

Full development and architecture references live under `plugins/common/references/`, reached from Common procedures.
They retain worked cases and decision criteria, not replacement summaries. Source-first investigation, TDD/SDD and selective DDD are shared procedures; consuming-project docs retain real structure/specs/ADRs
and local authority, not another methodology manual. Monorepos and single packages retain their own native layout
and package boundaries rather than adopting a required folder tree from this repository.

## Install, activate and update deliberately

Use [host setup](docs/hosts.md) with a local index or the reviewed Git source. Start with
selected skills only; hooks, MCP, assets and application connectors are not prerequisites. No MCP configuration is bundled.

Plugins enabled globally remain enabled unless the trusted project's configuration explicitly overrides their known
identity. Inspect the effective configuration and preserve unrelated user plugins and managed policy.
Installing a plugin, enabling it, trusting its hook, fresh-session discovery and correct task invocation are separate
checks. Versions are host-managed, not independent per-repository locks.

## Role adapters, not invented native support

Each bundle has a portable root `plugin.json` for Codex and a `.claude-plugin/plugin.json` adapter. Common also exports
Claude's native `agents/*.md` from the canonical role TOMLs. Codex currently does **not** register agents from plugins:
its canonical `exports/codex/agents/*.toml` are explicit optional provisioning artifacts, not auto-loaded roles.
Use built-in Codex agents by default; project-specific specialization belongs at native `.codex/agents/*.toml`.
Generic role bodies have one canonical source here. See [host support](docs/hosts.md).

## Maintain and verify

```bash
uv sync --locked
uv run --locked python scripts/build_plugins.py
uv run --locked python scripts/build_plugins.py --check
uv run --locked pytest
```

The builder uses only the standard library; Python and pytest support maintainer checks. Plugin installation uses
prepared files and does not invoke the provider builder. Most skills and the optional shell advisory need no Python.
`react-ui:ui-ux-pro-max` optionally uses an already available Python 3.9+ interpreter for local, stdlib-only data search;
missing Python is a reported limitation, not permission to install it. No search runtime, browser or application
execution is required for Markdown-only work. Do not run product applications or hardware to validate prose.

The [MIT License](LICENSE) covers original material authored and owned by Jongmoon Choi only. Imported material
retains its own licenses and notices; see [licensing and provenance](LICENSING.md) before reuse. A new release still
requires authorization and review of applicable rights, notices, and disclosure scope.

- [Release and rollback](docs/releases.md)
- [Source provenance and transformation](docs/provenance.md)
- [Host configuration and update boundaries](docs/hosts.md)
- [Frontend design and review workflows](docs/frontend-workflows.md)
- [Upstream selection audit](docs/upstream-audit.md)
- [Maintainer contract](AGENTS.md)

## Opt-in agent behavior evaluations

[Agent evals](docs/evals.md) live in `evals/`. `scripts/run_host_evals.py` compares native project skills using existing
Codex authentication and isolated Docker grading; `scripts/run_evals.py` runs both Codex/Claude inside disposable
containers. Both are opt-in. The evaluator tests check the harness offline and never call a model. Existing software
checks remain separate from observed skill reads, behavioral adherence and generated-code outcomes. No model eval is
added to ordinary PR CI, no host authentication is copied, and no automatic A+ score is awarded.
