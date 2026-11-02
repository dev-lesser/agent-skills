# Architecture judgment criteria

The goal is not the number of folders, but cohesiveness of responsibility, benefit to the caller, and locality of changes. This document is an overview. Specific project decisions and action agreements to be maintained follow the existing ADR/specification practices for the project. Check the available project guidelines and native manifest for the actual package and command. Common review criteria identify and confirm installed skills and resources that fit the scope of work. Examples do not mean that the functionality has been implemented.

## Repository groups and native package

Both standalone and monorepo distinguish responsibilities between application and reused packages by first looking at the actual package manifest, existing sources, and callers. The paths below are possible examples and do not require the same directory for each project.

| selected package | Native boundary example |
| --- | --- |
| Python | standalone `src/package_name/` ; `src/package_name/` in mono package, manifest and tests |
| TypeScript/React | package `src/` and `package.json` ; Resolution of the actual selected Node/browser/bundler |
| Rust | `src/lib.rs` + `src/main.rs` , `Cargo.toml` , features/targets and tests in the basic package |

For example, in a repository, `apps/api/` may be an execution unit and `apps/api/src/api_service/` may be a Python import source. A separate outer `src/` wrapper is not needed. Folders alone do not create a package, workspace, FFI, or deployment.  If `scripts/` or `bin/` exists, they are responsible for the maintenance/command entry point determined by the project. Unselected packages or empty domain layers are not created.

## Default: small package and clear responsibilities

For a small library, an easy-to-understand public API and internal modules are sufficient. A small API/service starts with a boundary transformation, a named operation, and a concrete I/O collaborator. The following relationships are examples of responsibilities, not commands that turn each item into a file or interface.

```text
entrypoint/composition -> boundary -> operation/policy -> concrete I/O collaborator
```

Extract the necessary boundaries when policies change independently, multiple I/O implementations, complex state invariants, or narrow tests require excessive setup. Preserves errors, validation, ordering and lifecycle before and after extraction. Use ABC, trait, generic repository or DI framework only when there is a real benefit to understanding boundaries.

## Complex backend is optionally domain-centric

- **Boundary** owns HTTP/CLI/message input, admission and external error/response conversions.
- **Use case/service** owns user tasks and orchestration and does not leak external framework objects to the policy.
- **Domain/policy** owns terms, invariants, and decisions. Do not include external I/O and framework dependencies inside.
- **Repository/adapter** owns the storage/external I/O contract and does not create a second business authority.
- **Composition** connects the resource lifetime with a specific collaborator.

This distinction is not a reason to create `domain/`, etc. in advance in the basic skeleton. Rather than redundantly defining the currently selected DTO/model in the name of purity, determine whether the framework needs to be removed based on actual test/caller costs. Rich domain and CQRS/event sourcing are selected separately when there is a basis to offset complexity.

## Worked example: report export

As an example, let's say the actual request is “Export a privileged report to CSV.” Initially, a named operation and an existing report reader/writer are sufficient. The following table is not an instruction to generate code, but rather a guide to how a contract leads to design and verification. API·CLI·UI includes only consumers who actually exist.

| responsibility | What to record/implement specifically | assertion to protect |
| --- | --- | --- |
| Spec | In `docs/specs/report-export.md`, the permitted subject, CSV result, empty report, and failure meaning are defined as proposed. | No permission means no write; Empty rows are header-only CSV; Write failure is not success |
| Use case | `export_report` / `exportReport` coordinates access confirmation, read, render and write | Actual export results and errors obtained with correct report/subject |
| Domain/policy | Owns only actual invariants, such as exportable report range and format | Rejection conditions and boundary values; Verify decisions without HTTP requests or storage clients |
| Boundary | Input, authentication, error mapping and public field preservation of actual API/CLI | Malformed format/permissions error is mapped to declared status/exit/result |
| I/O seam | The read/write and stream resource life of external storage is owned by the collaborator. | Adapter's actual temp-file/fake endpoint operation, failure cleanup and error preservation |
| Consumer | Existing UI/SDK/CLI interprets results and errors | Experience of success and failure through public contracts; Don't just check the number of internal method calls |

For example, Python's `test_export_report_without_access_does_not_write` , `test_export_report_with_empty_rows_writes_header` , and `test_export_report_when_write_fails_returns_error` are names that reveal different conditions in the spec. Other languages ​​also express the same behavioral boundaries with corresponding native test conventions. The side-effect assertion of not writing is an important contract for permission denial, and the success test also verifies the actual output.

**When is it a port?** Since Storage is the actual external I/O, there is a reason to separate policy testing and I/O verification by injecting a concrete writer. If existing collaborators are sufficient, do not create a new ABC/trait. When multiple interchangeable storage or stable external contracts are needed, narrowly specify the method·error·cleanup contract to support. It is not said that the actual adapter has been verified just by passing the fake.

**When is it a strategy?** When only CSV is needed, the `render_csv` function can be used. When an actual JSON export request is added and the format-specific behavior changes in the same input/result contract, the renderer can be selected as a callable or small mapping. Preserves existing CSV regression and adds JSON results, unknown format, and failure tests. Do not pre-create registries, factory hierarchies or classes for future formats.

**How ​​do I extend or change it?** Changing a public field like `output_format` updates the authority of the wire schema and all actual producer/consumer, export lists, fixtures, migration and native checks. After implementation and verification, synchronize the spec to current. If you see repeated modifications that require simultaneous changes to domain, API, and storage, first investigate responsibility leaks and overlapping contract authority. Similar file shapes alone do not create aggregates or shared frameworks.

## Frontend: feature and state ownership

An example of a React structure is `app -> features -> shared`. Here, `app` is the app combination, `features` is the user behavior, and `shared` is the common UI/function used by multiple actual consumers. The actual project structure and ownership come first. If connection between features is necessary, review the parent composition or actual shared responsibility rather than unconditionally importing each other.

The state is placed under a single authority as close as possible and the derived state is not stored redundantly. The server's original status, user input, loading/error/stale display, and domain determination are distinguished.  `useTransition`, memoization or provider introduction does not replace network cancellation or business authority. Only use APIs supported by the actual React/framework version, and preserve the applicable design brief and accessibility for visual work.

## Monorepo and cross-language agreement

Monorepo is a collaborative unit, not a runtime, dependency graph, or release unit.

| boundary | Decisions that must be specified |
| --- | --- |
| Python package/workspace | import name, `src/` packaging, interpreter, manifest/lock and native checks |
| TypeScript library/service/browser | consumer runtime, ESM/CJS, compiler/bundler resolution, exports/types and tests |
| Rust crate/workspace | library/bin target, public API, features/targets, toolchain/lock policy and native checks |
| Shared schema/event/API | canonical source, producer/consumers, units/errors/version/migration and compatibility |
| Native/FFI | Actual binding/ABI or CLI/transport method, ownership/errors, packaging and both verification |

`paths` alias is not a TypeScript package boundary or emitted import rewrite.  The existence of the `contracts/schemas` folder does not determine the schema language, code generation, or domain authority. Even if you place the Rust crate and Python package side by side, PyO3/Tokio/FFI does not automatically exist.

Changes are tracked by an integration owner across schemas, producers, all active consumers, fixtures, and each native environment. If there is no external consumer or verification is not possible, it leaves a limit. Byte matching of the same fixture is not executed interoperability, and native compatibility is not claimed just by passing a test in another language. When executing, select a contract/native procedure that matches the actual change boundary among available skills.

## Things to keep in mind while separating

Timeout/retry/idempotency, partial-startup cleanup, task cancellation, shutdown, untrusted input validation, and safety authority must not be lost during structural changes. Adding an abstract layer or log/ACK does not verify this property. It is confirmed through actual regression and separate review, and deployment/hardware is reported as separate evidence.
