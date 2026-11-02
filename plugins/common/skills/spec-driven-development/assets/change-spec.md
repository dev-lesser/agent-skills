# Change specification: <observable outcome>

The existing project form and storage location take precedence. If there are enough clear issue/task briefs, do not create duplicates. Contracts and interim plans to be maintained follow the location and preservation criteria established by the project. If any of the items below do not apply, write down the reason or remove them.

## Status and Contractual Authority

- Status: proposed / implementing / current / superseded
- Owner and current contract/alternative spec links:
- Implementation/verification basis and unverified scope:

## Outcome and scope

- Observable results and acceptance criteria:
- in scope / out of scope:
- owning packages and producer/consumer, external handoff:
- Each native runtime/toolchain, manifest, lockfile, and schema authority:

## Use cases and invariants

| Input·Subject·Status | expected outcome or rejection condition | invariant/error meaning | Protect behavioral assertion |
| --- | --- | --- | --- |
| <scenario> | <observable outcome> | <constraint> | <test boundary> |

For small tasks, this table can be replaced with sufficient acceptance items. In fact, it lists responsibility for divided boundary/use case/policy/I/O, but does not enforce folders/classes. If port/strategy is required, write actual external I/O, variant, public contract, and failure/lifecycle meaning. Do not create an interface for future virtual implementations.

## Consumer and native environment

| Producer/consumer | Original contract·public surface | manifest/lock·environment·gate | Change/Compatibility/External handoff |
| --- | --- | --- | --- |
| <owner> | <authority> | <native checks> | <migration or unavailable evidence> |

Do not add languages ​​or distribution units that do not apply. Do not assume FFI or common locks just because different languages ​​are in the same repository.

## Contracts to preserve and migration

- API/export/schema, identity/units/error/order/lifecycle compatibility:
- Data/security/safety boundaries that will not be changed:
- Migration order and existing/new version coexistence conditions:
- Source and edit boundaries for the generated/vendor area:
- When expanding an actual strategy/adapter, contract tests for existing/new variants:

## Verification

| Acceptance criterion | Verification layer/environment/actual command/data | expected result | Observation results/limitations |
| --- | --- | --- | --- |
| <criterion> | <evidence> | <expected> | <observed or not run> |

Select behavioral failing regression for new action/modification, characterization for preservation, and static checks for document/skeleton. The actual application gate is determined by the owning package, and this template does not provide virtual passing instructions. The sharing contract includes a separate review with all active consumers. Distinguish between software/deployment/physical evidence. Distinguishes between unit policy and actual adapter/integration evidence, and includes cases of invalid input, failure, deadline/cancel, and cleanup of changed boundaries. If you haven't observed the RED of an already existing implementation, do not hide that evidence gap.

## Sync with Rollback

- Rollback preserves data, caller, and safe state:
- Current specs/README/ADR to be updated after verification:
- Remaining proposal and external compatibility handoff:

Work that has been clearly approved is carried out without re-approval procedures. Release, publish, and live/hardware operations are separate permissions.
