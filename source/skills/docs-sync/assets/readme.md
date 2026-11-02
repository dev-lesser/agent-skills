# README: <package-or-folder-name>

Existing READMEs and project conventions take precedence. Fill in the necessary fields only when the responsibilities or usage agreement of the new package/folder are unclear. For simple folders, a short description of responsibilities and a link to the parent document are sufficient. Do not duplicate forms in all folders. Agent constraints apply to `AGENTS.md`, work procedures are linked to the selected skill and are not duplicated here.

## Purpose and Status

- Responsibilities and primary users/callers:
- Status: skeleton / implemented / deprecated
- What to include and what not to include:

## Boundaries and public surfaces

- Major subpaths, responsibilities, and authoritative owners:
- Actual entrypoint / public exports / API and private implementation:
- Allow dependency direction, external systems and authoritative schema and producer/consumer:
- Representative use case, state owner and invariant to be preserved:
- If there is an actual extension seam, the collaborator/strategy contract and error/lifecycle implications:

Describes the native layout of the actual language/tool. Check whether the repository is a single package or monorepo and do not guess the classification path. Do not fill in unselected framework/DDD layers, separate interfaces, or virtual extension points.

## Environment and use — only for executable packages

- Runtime/toolchain, manifest and lockfile are held in:
- Actual installation/execution commands and execution directories:
- Required settings, confidential information handling and lifecycle:

If it is the Skeleton step, do not imagine execution instructions but write down unimplemented decisions. Use `.gitkeep` only when you really need an empty directory and there is no responsibility that needs documenting. If the README already tracks it, don't add duplicate markers.

## Verification and Compatibility — Only on Changing Boundaries

- Affected import/export/schema, tests/docs and actual verification locations:
- Actual test/typecheck/lint/build commands and applied native environment:
- Location of public behavior, policy, adapter/native integration and consumer verification:
- Scope of support, error/compatibility agreements and known limitations:
- Procedure for changing contract tests and consumers to be preserved when adding a new variant/adapter/export:
- Separate approval and evidence if deployment or hardware validation is required:

Distinguish between command/file existence and actual passing results. Passing example tests or fakes is not reported as production I/O verification.

## Related documents

Add maintained spec/ADR, usage examples and actual relative links to parent documentation. Session logs for the same rule or date are not replicated.
