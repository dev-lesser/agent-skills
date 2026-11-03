# Local and shared plugin sources

A marketplace is a JSON index used by the host to resolve plugin identities. It is **not** a requirement to publish to
OpenAI's public directory or make this Git repository public. This checkout already includes both native indexes.

## First-run error: plugin not found

For `plugin X not found in marketplace dev-lesser-agent-skills`, check that the reviewed source has been registered.
If it has not, register it **once** on the host:

```bash
codex plugin marketplace add /path/to/agent-skills
```

Or, from the reviewed `agent-skills` checkout:

```bash
codex plugin marketplace add .
```

Then retry the selected plugin adds. If the marketplace name is already
registered, inspect source/revision/access instead of silently retargeting it. A wrong or stale same-name Git cache can
produce this symptom too; URL/ref changes alone do not prove the source used. Do not auto-register a replacement,
delete host caches or overwrite unrelated plugins to hide the failure.

Claude users register their reviewed source separately with `claude plugin marketplace add /path/to/agent-skills`.
Local delivery needs no remote. Keep the source checkout available; every developer/CI host needs its own access,
registration and refresh. Machine paths, caches, credentials and trust records do not belong in generated products.

## Install selected bundles

After registering the reviewed source, install only the bundles needed by the consuming project:

```bash
# Codex:
codex plugin add common@dev-lesser-agent-skills
codex plugin add python@dev-lesser-agent-skills
codex plugin list --marketplace dev-lesser-agent-skills
# Claude alternative; use the actual installation scope:
claude plugin install common@dev-lesser-agent-skills --scope project
claude plugin install python@dev-lesser-agent-skills --scope project
```

The commands consume prepared payloads; they do not run this provider's Python builder, install product dependencies,
initialize Git, or approve trust. Review and activate each host's configuration separately; installation, fresh-session discovery, invocation and observed behavior are distinct.

Most skills are instructions/resources only. UI UX Pro Max's optional local data search needs an already available
Python 3 interpreter and the standard library; it does not authorize a runtime install, persistence, browser or
application execution. See [frontend workflows](frontend-workflows.md).

## Git source

For a new registration using this public repository instead of the local checkout:

```bash
codex plugin marketplace add dev-lesser/agent-skills --ref main
claude plugin marketplace add 'dev-lesser/agent-skills#main'
```

Do not run this as an automatic replacement for an existing same-name registration. Git credentials, when needed for
other sources, use normal host/Git mechanisms; URLs do not prove a successful fetch, and credentials do not belong
in project files.

Codex can reuse an existing same-name cached Git marketplace even when a different source/ref is passed through
configuration or CLI overrides. Those values do not prove the actual fetched source or installed bytes. Deliberately
register/refresh and inspect source/cache identity before manual installation. `stable` is a reviewed moving channel
only when maintained, not an independently verified payload lock.
Local or Git delivery does not require a directory submission. Actual release, authentication where applicable,
and hosted CI results require their own evidence; these commands do not certify App/Claude discovery.

## Activation is not trust or adherence

A trusted Codex project can override
host defaults; untrusted projects can ignore those overrides. Preserve unrelated user plugins and managed policy.
A monorepo selects a union; project routing chooses the actual owning package's procedures. This is not a model sandbox.
Native installation is host-scoped and globally enables selected identities; project flags apply only after project
trust. Repeated adds use native cache/installation behavior, not independent per-project versions. Shared releases still
refresh through the host.

Flags alone are not installation/discovery proof. Host startup synchronization can be asynchronous, and refresh can
fetch/install configured disabled plugins too: false controls loading, not a no-download guarantee. Inspect effective
installed versions and start a fresh session before relying on discovery. App/CLI/IDE support differs.

## Optional hooks and native agents

`session-guidance` is separately opt-in and off by default. Its SessionStart hook is POSIX printf-only: no scan, network,
tests, permission mutation, services or hardware. Installation/enablement does not grant hook trust; review definitions
through `/hooks` where supported and respect hook-disable policy. Never override personal trust records.

Each package has portable root `plugin.json` for Codex and `.claude-plugin/plugin.json` for Claude. `.codex-plugin` is
an optional compatibility location, not a consumer directory for selected skills.
Common's generated Claude-native `agents/*.md` derive from canonical `plugins/common/exports/codex/agents/*.toml`.
Those TOMLs are optional explicit provisioning artifacts: Codex 0.160.0 and the inspected bundled 0.162.0-alpha.17.2 do not load agents from plugins.
Use built-in Codex agents by default; custom roles require separate native `.codex/agents` provisioning. A skill's
`agents/openai.yaml` is interface metadata, not custom-agent registration.

## References and limits

- [OpenAI local/private catalogs, packaging and registration](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work)
- [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [Claude commands and local/private sources](https://code.claude.com/docs/en/plugins/cli-reference)
- [Releases, refresh and recovery](releases.md)

Isolated native CLI installation/configuration checks are not actual App/Claude discovery, model invocation/adherence,
host hook execution, hosted CI, deployment or physical validation. No personal host configuration was changed.
