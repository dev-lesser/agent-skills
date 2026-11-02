# Task brief: <outcome>

Priority is given to the existing project form and storage location, and the relevant items are filled in only when there is a necessary handoff.

## Outcome and scope of ownership

- Observable completion conditions:
- owning package/files and integration owner:
- Affected callers/contracts/consumers:
- Exclusions and allowed side effects:
- Representative use case and invariant to preserve; actual responsibility/I/O/variant seam:

## Precise instructions to read

- Applicable `AGENTS.md` and package README:
- Required organization plugin/task `SKILL.md` entrypoint and specific constraints to apply to that task:
- native environment/toolchain/manifest/lockfile and safety/lifecycle authority:

Simply writing down the role name is not a basis for skill selection. Do not add skills that are not applicable.

## Evidence and handoff

- Check caller/tests/fixtures/config/exports before changing:
- Choose between behavioral regression / characterization / static evidence:
- Success/error/lifecycle assertions for existing/new variants and public contracts:
- Focused checks and actual package completion gates, or explicit execution exclusions:
- Compatibility, rollback and external verification limitations:
- Boundaries requiring independent review and specific failure conditions to be identified by the reviewer:

If it is a parallel task, it notifies the presence of another worker and entrusts the shared file to the integration owner. Report conflicts and blockers without reverting someone else's changes. Child tasks are not re-orchestrated without separate permission. Upon completion, it reports changed files, actual observed check results, omissions/risks, and rollback.
