# Source provenance and closed payloads

DevLesserAgentSkills maintains **39 procedures in 11 bundles**, including six React UI skills. This personal
distribution excludes robotics and firmware bundles. Historical upstream extraction and evaluation observations
remain historical evidence, not verification of this repository or its current release.

## Plugin-owned canonical inputs

Edit complete procedures and their local resources at `plugins/<bundle>/skills/<skill>/`. The v2 ledger at
[`provenance/skill-sources.json`](../provenance/skill-sources.json) records repository-root-relative canonical paths,
immutable source revisions, original upstream hashes, derivation evidence and reviewed local hashes. Initial
extraction was uncommitted; do not invent a source Git revision or replace historical evidence with a new origin.
`catalog.json` owns the release version, stable bundle identities and exactly one owner per skill.

Shared references and third-party license/NOTICE files also have one canonical plugin owner declared by the ledger.
Other bundles receive generated closed-package copies. Resolve that owner before editing; an old destination copy
is never the source for preparation. Root `LICENSE` and `LICENSING.md` are the sole legal-policy inputs, with reviewed
ledger hashes; copies at plugin roots are generated. There is no parallel `source/` authoring tree or root hook mirror.

A canonical hash mismatch stops preparation until the change is independently reviewed and its local hash recorded.
Do not change immutable upstream hashes to approve an adaptation. Preserve complete procedure bodies, resources,
notices and true historical derivation; a count or a passing check is not permission to remove them.

## Preparation, not installation

`scripts/build_plugins.py` validates canonical inputs and prepares declared generated files and both marketplace
indexes. A consumer installs these prepared payloads; plugin add does not invoke this provider's Python builder.

Preparation follows explicit ownership and closure rules:

1. Keep each canonical skill tree under its one owner, with complete procedure and resource bytes.
2. Keep same-bundle resource links local. Cross-bundle skills use stable `bundle:skill` identities and selection notes;
   composition metadata does not install dependencies.
3. Express declared project-context paths as lookups in the **consuming repository**, not assumptions that every
   project has a particular README, structure, spec or ADR layout.
4. Resolve reached shared references from their registered canonical owners. Generate destination copies with only
   declared portable link transformations; preserve full worked examples rather than summaries.
5. Include the selected sources' recorded license/NOTICE evidence. Reject missing resources, unknown outward paths,
   undeclared plugin files, malformed frontmatter, managed symlinks and incorrect managed path types.
6. Stage and validate expected output before replacing changed generated files. Never overwrite canonical inputs,
   delete unknown files or replace the entire `plugins/` tree. On a caught update failure, restore prior generated
   files; if restoration fails, report and retain the recovery directory. This is not crash-atomic release publication
   or a sandbox against concurrent filesystem changes.

Markdown links inside fenced code examples remain examples, not resource declarations. External documentation links
remain external; local closure checks do not establish remote availability or current correctness.

## Separate hashes for separate claims

Each generated `provenance.json` filters selected source/license records and records:

- `upstream_sha256`: original upstream bytes at an immutable revision;
- `source_sha256`: reviewed canonical local bytes;
- `payload_sha256`: actual packaged bytes;
- `canonical_source`: the repository-root-relative owner path, alongside retained derivation evidence.

For an unchanged canonical plugin-owned file, source and payload hashes match. A generated destination copy can have
a different payload hash because its declared links were rewritten. `artifact-hashes.json` covers actual package
files except itself. These hashes detect stale or changed bytes; they do not prove source selection is safe, a host
loaded a skill, an agent complied or a product improved. Installed links close within their package, not another
plugin cache or this Git root.

## Licensing and distribution boundary

The root [MIT License](../LICENSE) applies only to original contributions authored and owned by Jongmoon Choi. It does
not replace imported or historically derived material's applicable terms and notices. See [licensing](../LICENSING.md)
for the scope and third-party evidence. Release review includes applicable rights, attribution, modification notices,
trademarks and disclosure scope. Passing local checks are not legal clearance or authorization to publish.

## Shared resources, roles and advisory hook

Common owns the full shared development, architecture and engineering references; Rust owns its recorded Rust
reference. Reached copies travel with other bundles. Project specs, ADRs, commands, authority and actual directory
layout stay with the consuming project; examples in shared references do not mandate a folder tree or runtime.

Four model-free role TOMLs live at `plugins/common/exports/codex/agents/`. They are canonical optional provisioning
artifacts. Common's `agents/*.md` are generated Claude adapters, not another authored role library. Neither TOMLs
nor a skill's `agents/openai.yaml` establish Codex plugin agent registration.

`plugins/session-guidance/hooks/session-start.sh` is the canonical opt-in printf-only advisory; `hooks/hooks.json`
inside that plugin is generated. Installation, activation and hook trust are distinct, separately reviewed steps.

Common's task/change forms stay under their owning skill `assets/` directories. Docs Sync owns the combined
package/folder README guide; Domain Modeling retains the upstream `ADR-FORMAT.md`. Existing consuming-project formats
and filled records remain authoritative; these assets do not require documentation for every task or folder.
`authored_skills` and `authored_resources` retain reviewed local hashes without inventing upstream authorship or
licenses. The root legal policy, not a generated provenance category alone, determines the original-material grant.

## UI UX Pro Max import

The React UI addition pins the MIT source at `713eef51b04efc98d6fa565323b495f7c9c89fd4`. It keeps the selected full
search data, four standard-library runtime modules and two text references, with recorded local adaptations and
upstream/local hashes. It excludes upstream installers, host adapters, hooks and browser tooling. See
[frontend workflows](frontend-workflows.md) for existing-runtime, read-only search, framework and persistence limits.
Data/search errors abort rather than becoming verified recommendations; persistence guards are managed-path
preflight checks, not a race-proof filesystem sandbox. Packaging checks do not establish fresh-session invocation,
UI quality or rendered/interaction correctness.
