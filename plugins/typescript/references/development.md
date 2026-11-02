# development workflow

This document is a shared development standard for installed common plugins. Do not copy the same instructions from project to project. Check the current package, provided functions, and actual commands in the applicable project guidelines, documentation, and native manifest. The naming, design, and review resources of shared skills and common plugins for each task are selected according to the actual task boundaries. Documentation alone is not evidence of execution or model adherence.

## Categorize tasks first

| work | minimal completion boundary | evidence |
| --- | --- | --- |
| investigation/review | Verify contracts with sources, callers and separate conclusions/uncertainties | Specific routes, failure conditions and reasons; No unnecessary modifications |
| document/skill/skeleton | Update requested files and references together | Review metadata, local links, provenance/licenses, entire file/whitespace |
| Behavior changes/bug fixes | Expected behavior → actual failing assertion → minimal modification | focused regression and owning package gate |
| Behavioral conservation refactor | Existing behavioral characterization → extraction | Preserve error, branch priority, lifecycle and integration coverage |
| Share contract/concurrency/safety | Short spec, owner·consumer·environment guidance | Separate review of each native gate and boundary cases |
| Generator·manifest·execution automation | Actual input/output and native environment contracts | Operation/error/consumer verification of generated results; prose-only exception does not apply |

Runtime/build/deployment/CI settings are the scope of application verification, not documents. Conversely, do not install apps or run services, CI, or hardware to only edit documents. Work that has been explicitly permitted is completed without asking for the same approval again. Work permissions for commit, publish, external state changes, and live/hardware access are checked separately.

## SDD, TDD, optional DDD

**SDD — specification-driven development:** In meaningful behavior/compatibility change, the outcome, invariants and acceptance are first clarified. The input, result, and failure meaning of the specification must be observable in the test. Small modifications can be completed with a sufficient issue/task brief, and change spec (shared skill `common:spec-driven-development`; select the `common` bundle when that task boundary is in scope) can be used when coordinating multiple packages or protocols. Maintained contracts are placed in the project's existing specification locations and practices and distinguish between proposed/implementing/current/superseded status. After verification, the actual contract is synchronized and unimplemented intents are not marked as currently supported. Spec Kit/OpenSpec installation and documentation of all operations are not required.

**TDD — test-driven development:** New behavior/bug fix is ​​implemented after confirming that the assertion of the behavior fails. An import failure or broken fixture does not reproduce a bug. The behavior to be preserved uses characterization, and prose uses static check. For the sake of formality, we do not run application tests on documents to make them RED. If you already have an implementation, make sure you can safely reproduce the baseline and be honest about any gaps in evidence. Do not create a RED by deleting someone else's implementation or claim a past RED that you did not observe.

**DDD — domain-driven design:** Choose where state ownership, terminology, invariants and reasons for change are truly complex. Do not add aggregate, repository interface, CQRS, and event sourcing to small CRUD/services all at once. DTO sharing and business authority sharing are different. You can see the application unit in [worked example](architecture.md#worked-example-report-export), which connects one export use case to the spec·invariant·test·actual I/O seam.

## Short loop before and after implementation

1. Write down the scope, owning package/files, caller/consumer, exclusions, and acceptance. The scope of influence extends to import/export, fixtures, config, generated source and native environment.
2. Only reads the current code/contract and the corresponding shared skill, leaving a short list of specific constraints to apply. If it is a defect, check the common cause with sibling callers of the same mechanism, and fix the smallest common cause for which there is evidence.
3. Prepare regression/characterization/static evidence appropriate for the type of change and make the smallest complete correction. In a single public action, it verifies success as well as invalid input, failure, and cleanup on its boundary.
4. Performs focused checks and declared completion gates in the actual package environment. Even if there is a common root command, ownership of the package-native gate and language-specific compatibility evidence are not omitted.
5. Significant contract/concurrency/safety changes are reviewed by a separate reviewer for failure conditions and evidence. Self-checks by the same author are not called independent reviews.
6. Align README/current specs with actual results and report change boundaries, observed checks, omissions, risks, and rollbacks.

Independent tasks can be parallelized with clear file ownership. Modification of shared schema/shared documents and dependent tasks are coordinated by the integration owner. Do not revert changes made by other workers.  Use Task brief template (shared skill `common:writing-plans`; select the `common` bundle when that task boundary is in scope) only for necessary handoffs.

## Verify when testing and scaling

- The test checks the actual results, status, and errors through Arrange-Act-Assert. The number of Mock calls alone does not prove success. Time, random, and external I/O are controlled by narrow collaborators or existing fixtures, and resources owned by each test are organized.
- Pure policy is confirmed through a quick unit test, actual storage/transport operation is confirmed through adapter/integration test, and user/consumer contract is confirmed through API/CLI/UI/package-boundary test. All tests do not require a DB or entire service stack.
- When adding a new strategy/adapter, reuse the success/error/lifecycle tests of the existing public contract and only add the differences in the new implementation. If it is a new wire field/export, check the producer·consumer·fixtures·docs and the old version compatibility path.
- When shared-state, deadline, cancellation, partial startup, and cleanup are changed, failure cases are added. Coverage ratio or number of tests are not a substitute for assertion quality and do not force new thresholds without evidence.

## Native environment and actual gate

The declared runtime/toolchain, manifest·lockfile, and check command are owned by the corresponding package. If not, determine the support environment within the scope of implementation, pin it, and then add the actual gate. Do not mix Node/React settings with Python packages. Upgrading or ad-hoc installation to match the latest version used in the example is not used as a basis for verification.

During iteration, focused checks are made and upon completion, the declared package/repository gate is executed. Root orchestration does not replace native verification of each language. If you observe other failures, report the cause and effect and do not quietly rule them out. If there are no commands or execution is excluded, do not create a pass result, but leave the necessary verification and reason for non-execution.

Verification results are divided into **static / software-tested / deployed / physically validated**. The existence of a skill file/role setting is not evidence of fresh-session discovery, automatic selection, or model adherence.

## Source-first development

First check the existing source·callers·tests·manifest·lock and the actual execution contract and distinguish between facts and proposals. Connects to observed contract and reason for change → specification/acceptance → behavioral test → minimum implementation → consumer confirmation. Here, source-first is a working principle and does not claim to be a separate standard methodology or other definition of SDD. SDD stands for specification-driven development defined above.

## Reference approaches

- [Spec Kit existing projects](https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md): Apply the specification while preserving the rules and current implementation of the existing project.
- [OpenSpec concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md): Distinguish between maintenance contract and change intention.

It is a reference approach and does not require CLI installation, new formats or approval rituals.
