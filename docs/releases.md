# Releases, refresh and recovery

Historical upstream releases are not releases of this personal repository. Local indexes do not require a public
plugin directory listing, and all distribution must honor recorded source licenses and access rights. The root MIT
license covers original material authored and owned by Jongmoon Choi; see [licensing and provenance](../LICENSING.md)
for its scope and third-party terms. New commits, tags, pushes, releases and visibility changes require current
task-specific authorization and appropriate license/proprietary-scope review. Record observed publication
and CI results separately; this document does not claim a release was made.

## One source, one release version

1. Edit canonical procedures/resources in their owning `plugins/<bundle>/` paths, not generated destinations. Root
   `LICENSE` and `LICENSING.md` remain the legal-policy inputs. Preserve upstream revisions/licenses and separately
   review changed local hashes in `provenance/skill-sources.json`; never auto-approve them. Keep stable plugin identities
   after first publication.
2. Update `catalog.json` version and matching `pyproject.toml`; run `uv lock` **without** `--upgrade` and review pins.
3. Prepare generated plugin files, run locked pytest and builder `--check`, then review artifact/provenance/license
   diffs. Release notes name changed triggers, compatibility, hook changes, observed checks and omitted host/session evidence.
4. With release authorization, commit and tag the reviewed commit as immutable `vX.Y.Z`. Validation rejects a
   tag that differs from the canonical catalog/package version. Do not move old release tags.
5. If an approved moving **`stable`** channel is maintained, promote only a validated release commit to it; `main` is
   development. Otherwise advance a registered immutable ref deliberately. Pushing a tag alone does not move the
   channel, retarget hosts, update installed plugins or reload sessions.

All bundle manifests use the one catalog version; Claude marketplace entries do not repeat it. Changes to public
plugin identities require coordinated consumer migration and review.

Preparation validates and stages the complete expected output before updating only changed generated files.
Canonical inputs remain untouched. A caught replacement failure restores prior generated files; if restoration fails,
the error identifies retained recovery files. Preserve that evidence and inspect the reported paths before retrying.
This rollback is not crash-atomic publication or a consumer install transaction. Never replace the whole `plugins/`
tree as recovery: it contains canonical inputs. Unknown files and managed symlinks fail preflight rather than being
deleted or silently adopted. Host installation consumes prepared payloads, not an on-install Python build.

## Host updates

Projects choose their own activation flags and use the index already registered on each host. A local index follows
its accessible checkout and reviewed generated artifacts; it has no imaginary Git channel. When using a Git source,
a reviewed moving `stable` channel can advance shared updates without editing every project selection. Immutable refs
are an explicit freeze. Neither source choice is a per-project installed-version lock when hosts share identity/cache.

### Moving channel versus pinned revision

A version change on `main` is not a broadcast to product repositories or developer machines. The provider must update
`catalog.json`, matching package/lock version and generated plugin manifests; editing skill text without a new manifest
version is not a reliable installed-payload update. An already enabled bundle keeps its stable identity across releases.

| Registered source ref | What a host refresh can receive |
| --- | --- |
| `main` | The reviewed current `main` commit, including rebuilt manifests |
| Maintainer-managed moving `stable` | A release only after the channel is deliberately advanced |
| Immutable release tag or commit | The same frozen payload; a new version elsewhere does not retarget it |

For a **new** host registration that deliberately follows `main`:

```bash
codex plugin marketplace add dev-lesser/agent-skills --ref main
```

An existing same-name registration must be inspected first. Re-running an add or changing a project ref is not proof
that its cached Git source was retargeted. Deliberate channel changes are separate from routine refresh. Prefer an
actually maintained reviewed release channel when that is the team's policy; `stable` is not created automatically.

For a Git-registered Codex index:

```bash
codex plugin marketplace upgrade dev-lesser-agent-skills
codex plugin list --marketplace dev-lesser-agent-skills --json
# Verify installed versions, then start a fresh Codex session.
```

A historical upstream Codex **0.164.0** Git-source compatibility check observed an installed `common` payload change from
`0.1.0` to `0.1.1` during marketplace upgrade when following `main`; a registration pinned to `v0.1.0` remained frozen,
even after re-adding the plugin. This establishes that historical client/scenario only, not this personal repository, universal automatic timing or other clients.
Inspect every selected installed version rather than treating a successful snapshot refresh as unconditional payload
proof. See [native marketplace commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin-marketplace).

Already-enabled product repositories need no new product commit merely for shared skill text changes when bundle
identities and selection stay the same. Each developer/agent/CI host refreshes its own source and installed payloads.
Selection/routing changes and migration from customized local Markdown are separate reviewed product changes; a host
refresh never retires those local files.

For local Codex sources, rebuild reviewed artifacts/version, follow the selected-install/refresh flow and inspect
installed metadata; Git marketplace upgrade is not a local-checkout publication mechanism.

For Claude, refresh both the listing and each selected installed plugin, then reload/start a new session. These are
reference commands; Claude execution remains unverified here:

```bash
claude plugin marketplace update dev-lesser-agent-skills
claude plugin update common@dev-lesser-agent-skills --scope project
# Use the actual installation scope (project/user/local); repeat for other selected bundles.
claude plugin list --json
# Start a fresh session, or use /reload-plugins where supported.
```

Third-party auto-update stays off unless the user/team deliberately opts in. Inspect effective installed versions and
fresh-session discovery; configuration or a catalog listing is not model-invocation proof. Other developer/CI hosts
need their own refresh. Changed hook definitions still require separate trust; never overwrite that personal state.

## Recovery

For first-run `plugin X not found in marketplace dev-lesser-agent-skills`, use [source registration recovery](hosts.md#first-run-error-plugin-not-found).
Register the reviewed source once only if missing, then retry the selected plugin adds.
An existing same-name source must be reviewed, not silently replaced; stale Git caches are not fixed by changing URL/ref alone.

Prefer **fix-forward**: publish a new version restoring prior approved content, validate it and promote that release.
This changes the cache version without rewriting tags/history. Historical source downgrade is a separate tested host
operation, not a promised per-repository rollback. Do not edit caches or overwrite unrelated personal/project settings.
Existing sessions may retain old instructions until reloaded. Review local copied-skill customizations before any
manual migration from old draft templates; no automatic destructive retirement is provided.

## Validation workflow

`.github/workflows/validate.yml` limits its built-in token to read-only permissions and uses immutable action SHAs. It runs locked tests, deterministic
artifact checks and tag/catalog/package/lock agreement; it does not publish, deploy, grant trust or contact hardware.
The workflow runs without cross-repository credentials or product deployment. A successful run establishes only the
executed checks for that commit; inspect individual job and skip results before reporting them.

Isolated local registration/flags-only and file-Git/cache tests do not establish private authentication, actual CI results, App/Claude discovery,
model adherence, hook trust or production safety. Those remain separately observed release acceptance layers.
