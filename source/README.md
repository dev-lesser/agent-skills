# Canonical procedure source

This directory owns 38 complete reusable skill trees, portable engineering references, source provenance/licenses
and generic role definitions. Optional reusable forms live in their owning skill assets, not a second templates tree. Imported skill bodies/resources retain their reviewed bytes; two earlier additions are documented
in the [upstream audit](../docs/upstream-audit.md). Consuming projects own their setup and project-specific rules.

Edit canonical procedures under `skills/`, not generated release artifacts. Follow the
[maintainer contract](../AGENTS.md), [task pointers](#task-pointers) and [provenance rules](../docs/provenance.md).
The raw tree is not a host installation directory: install closed `plugins/` payloads through the native marketplace.

Raw skill links can denote consuming-project context. The builder's explicit context map converts those to project
lookups; portable engineering/methodology/Rust references and license/provenance resources are bundled locally. Undeclared
outward paths fail generation. Neither the source layout nor examples override a consuming project's authority.

Generic roles live once in `agents/*.toml`. Generated Claude agents are native adapters; generated Codex exports
require explicit separate provisioning. Codex plugin role auto-loading is not supported in the inspected clients.

## Canonical skill task pointers

First check [Maintainer contract](../AGENTS.md) and the current request and change owner. This path is a common source. The generated plugin is installed on the host; consuming projects keep their own project-specific guidance. Plugin ownership is managed by [catalog](../catalog.json), and the original/modified hash is managed by [manifest](skill-sources.json).

## Required skill selection and evidence

1. Only the exact entrypoint corresponding to the actual task is read, and detailed references are read from the corresponding branch.
2. AGENTS·package manifest·lock·command·safety contracts from existing projects take precedence over the example.
3. Explain what criteria influenced your decision. File existence, installation, new session discovery, invocation, and compliance are separate.
4. Independent work is given proprietary files, precise instructions, and verification standards, and changes made by others are preserved.
5. Behavioral changes are verified with regression, preservation with characterization, and documentation with static checks.

## Task pointers

| task/boundary | Accurate local entrypoint |
| --- | --- |
| Design/review of API·wire contract·error meaning | [api-design-principles](skills/api-design-principles/SKILL.md) |
| Select/change responsibility/SRP/hierarchy/DDD/dependency direction | [architecture-patterns](skills/architecture-patterns/SKILL.md) |
| Actual Python async changes; cancellation·deadline·backpressure | [async-python-patterns](skills/async-python-patterns/SKILL.md) |
| Research current recommendations/external implementations; official/upstream evidence first | [best-practice-research](skills/best-practice-research/SKILL.md) |
| Comparison of options for requirements and designs that have not yet been decided | [brainstorming](skills/brainstorming/SKILL.md) |
| independent code review; Location/Failure Condition/Severity/Minimum Correction | [code-review-excellence](skills/code-review-excellence/SKILL.md) |
| Cohesive module·interface·test seam·commonization·scalability judgment | [codebase-design](skills/codebase-design/SKILL.md) |
| Remove public names/APIs/implement compatibility; External consumer confirmation | [deprecation-and-migration](skills/deprecation-and-migration/SKILL.md) |
| Domain terminology, ownership, invariants, and existing glossary/ADR summary | [domain-modeling](skills/domain-modeling/SKILL.md) |
| Compliance with current code/specification/README/agent guidelines | [docs-sync](skills/docs-sync/SKILL.md) |
| FastAPI app/router·Input validation·dependency/lifespan·HTTP boundary change | [fastapi-backend](skills/fastapi-backend/SKILL.md) |
| Create/redesign requested visual UI; Prioritize existing design guidelines | [frontend-design](skills/frontend-design/SKILL.md) |
| Requested UI audit·polish·loading/error/a11y hardening | [impeccable](skills/impeccable/SKILL.md) |
| Litestar handler/router·Explicit DI·lifecycle·HTTP boundary change | [litestar-backend](skills/litestar-backend/SKILL.md) |
| Schema·producer/consumer changes across multiple packages/languages | [monorepo-contract-change](skills/monorepo-contract-change/SKILL.md) |
| NestJS modules/providers·DTO verification·controller·HTTP lifecycle change | [nestjs-backend](skills/nestjs-backend/SKILL.md) |
| Next.js App Router·server/client·Route Handler/Action·Cache boundary change | [nextjs-app-router](skills/nextjs-app-router/SKILL.md) |
| ground truth diagnostic gap/requested logs/metrics/traces; redaction bounded cardinality | [observability-and-instrumentation](skills/observability-and-instrumentation/SKILL.md) |
| Minimum complete solution before implementation/refactoring/adding dependencies/abstractions | [ponytail](skills/ponytail/SKILL.md) |
| Python SRP·KISS·composition·specific collaborator·optional pattern | [python-design-patterns](skills/python-design-patterns/SKILL.md) |
| Input validation, exception meaning, partial failure, call boundary | [python-error-handling](skills/python-error-handling/SKILL.md) |
| Python import·src layout·public API·packaging boundary | [python-project-structure](skills/python-project-structure/SKILL.md) |
| Failure to own/partially start/clean up connections/files/task | [python-resource-management](skills/python-resource-management/SKILL.md) |
| Python annotations·generics·Protocol·version and boundary of existing checker | [python-type-safety](skills/python-type-safety/SKILL.md) |
| pytest fixtures · Test boundaries · Actual errors/invariant regression | [python-testing-patterns](skills/python-testing-patterns/SKILL.md) |
| Task ownership·shutdown·backpressure in Rust async is explicitly selected | [rust-async-patterns](skills/rust-async-patterns/SKILL.md) |
| Rust ownership·Result·visibility·traits·native checks | [rust-best-practices](skills/rust-best-practices/SKILL.md) |
| trust boundary·auth·sensitive data·untrusted input | [security-and-hardening](skills/security-and-hardening/SKILL.md) |
| Synchronization of acceptance criteria and specifications for meaningful behavior/compatibility changes | [spec-driven-development](skills/spec-driven-development/SKILL.md) |
| Reproduce defects and track common causes in callers/contracts/sibling modules | [systematic-debugging](skills/systematic-debugging/SKILL.md) |
| Change action is RED/GREEN, preservation is characterization, document is static | [test-driven-development](skills/test-driven-development/SKILL.md) |
| Node/browser·ESM·exports·strict types·actual import graph | [typescript-project-structure](skills/typescript-project-structure/SKILL.md) |
| Change React component API·composition·state ownership | [vercel-composition-patterns](skills/vercel-composition-patterns/SKILL.md) |
| Change rendering/data/performance of selected React/framework version | [vercel-react-best-practices](skills/vercel-react-best-practices/SKILL.md) |
| Check commands, output, and omissions in the actual range just before completion assertion | [verification-before-completion](skills/verification-before-completion/SKILL.md) |
| UI interaction·keyboard/focus·semantic·accessibility review | [web-design-guidelines](skills/web-design-guidelines/SKILL.md) |
| skill·AGENTS·conditional routing design; progressive disclosure | [writing-for-agents](skills/writing-for-agents/SKILL.md) |
| Division of owned files, interfaces, and verification of confirmed multi-step requests | [writing-plans](skills/writing-plans/SKILL.md) |

[Engineering criteria](references/engineering.md) provide shared guidance on SRP, KISS, naming and dependency direction.
Read [development](references/development.md) for workflow and verification, [architecture](references/architecture.md) for design decisions, and [Rust criteria](references/rust.md) for Rust changes. These shared instructions are not copied into consuming projects. Runtime, toolchain and version decisions remain with the owning project; examples do not authorize installation or deployment.

## Roles and maintenance

Common roles are created from one source: [architect](agents/architect.toml) , [executor](agents/executor.toml) , [code-reviewer](agents/code-reviewer.toml) , and [verifier](agents/verifier.toml) . We don't force you to assume your role for every task.  Check [Host support](../docs/hosts.md#optional-hooks-and-native-agents). Do not confuse Claude native adapter and Codex explicit export with auto-registration.

If you change the original, the immutable upstream record and the reviewed local hash are kept together and the plugin is regenerated.  [Verification, releases and host updates](../docs/releases.md) is independent of changes in consuming projects. A clear scope of approval is not asked repeatedly; committing, publishing, distributing, and performing each require actual permission.
