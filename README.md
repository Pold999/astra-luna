# Astra-Luna

> Let Astra think about the hard parts. Let Luna do the work.

A small Codex skill for cost-aware, model-aware task execution:

```text
substantive task
      |
      v
  Astra plans  --->  Luna implements  --->  Astra verifies
```

`astra-luna` routes the expensive reasoning work to `gpt-6-astra` and keeps repository exploration, edits, commands, and routine debugging in `gpt-5.6-luna`. The same Astra advisor checks the real changed files and test evidence after execution, with one bounded repair round when needed.

## Why it exists

Using Astra for every shell command, file read, and edit is powerful but expensive. Using Luna for every decision can be cheap but brittle on ambiguous, cross-file work. This skill keeps Astra at the decision points where it adds the most value and lets Luna handle the high-volume execution loop.

It is a routing policy, not a magic model switch. Select Luna as the main task model; the skill cannot change that setting for you. Simple questions and tiny obvious edits stay direct. The workflow is intentionally bounded and reports when the host cannot provide the required model or collaboration tools.

## What it promises

- Compact handoffs instead of copying an entire conversation.
- One reusable Astra planner/verifier instead of separate expensive agents.
- Actual-file verification, not acceptance of the executor's summary alone.
- At most one repair round, so a bad patch cannot create an infinite token loop.
- Explicit `PASS`, `FIX_REQUIRED`, or `UNVERIFIED` outcomes.

## Token savings

The repository does not hard-code a marketing percentage. On the included tiny smoke task, Astra-Luna used at least `6.54x` the pure-Astra tokens because planning and verification dominated the work. That negative result is intentional evidence: this workflow is for substantial tasks where a long Luna execution loop can amortize Astra's decision calls, not four-test edits. See [`docs/benchmark.md`](docs/benchmark.md) for the raw token records and limitations.

## Install

Copy this folder into your Codex skills directory:

```bash
cp -R . ~/.codex/skills/astra-luna
```

For automatic matching, add the routing rule from `AGENTS.md` to the instruction file used by your Codex environment. Then select `gpt-5.6-luna` as the main task model. You can also invoke it explicitly:

```text
$astra-luna Fix the failing import path and run the focused tests.
```

## Scope

The skill does not grant permission to publish, allocate compute, access credentials, or perform destructive operations. It preserves project-local instructions and reports unavailable tools or unverified claims instead of silently substituting models.

## License

MIT. See [`LICENSE`](LICENSE).
