---
name: astra-luna
description: Use for substantive coding, debugging, research with execution, and artifact creation to reduce expensive-model work through Astra planning, Luna execution, and Astra verification. Also use when explicitly invoked as $astra-luna. Skip automatic orchestration for simple questions, lookups, and tiny edits. Intended for a Luna main task with model-selectable collaboration tools.
---

# Astra Plan, Luna Execute, Astra Verify

Keep routine interaction, implementation, commands, and testing in the Luna main task. Delegate decisions and final verification to one reusable Astra advisor. This reduces expensive-model work, not necessarily total tokens or cost by a fixed amount.

## Entry and Preconditions

- Automatically apply to substantive execution where planning and verification justify the handoffs. Answer simple questions and lookups, and perform tiny, obvious edits directly. Explicit `$astra-luna` requests opt into the workflow even for a small task.
- Skip recursive orchestration only inside an actual collaboration child assigned an advisor or executor role. An existing desktop task resumed by cross-task messaging remains a main task; a handoff message is not evidence that it is a child agent.
- Automatic invocation depends on the host's skill selector or an explicit standing instruction in AGENTS.md; neither is a guaranteed runtime hook. Do not change global instructions, configuration, or model defaults unless the user explicitly requests that configuration.
- The intended main model is `gpt-5.6-luna`. A skill cannot change the main task model. If the main model differs or cannot be established, disclose that the Luna-main cost condition is unmet or unverified. Do not claim a complete cost-saving chain.
- Require tools that can select `gpt-6-astra` with `high` reasoning and reuse its agent ID. If unavailable, report the exact limitation. Do not silently substitute models or invoke a CLI/API workaround.
- Preserve project instructions, specialist skills, existing changes, and authorization boundaries. This skill is not authorization for publishing, credentials, payments, or destructive operations.

## Host Tool Compatibility

Use tools actually exposed in the current task. The preferred API is the independent `collaboration` namespace. Some desktop tasks expose equivalent `multi_agent_v1__*` tools inside `functions.exec`; inspect their schemas before use. A verified legacy spawn uses `model: "gpt-6-astra"`, `reasoning_effort: "high"`, `fork_context: false`, and `message`; reuse the returned advisor with the host's continuation tool. Do not infer availability or arguments from names alone.

## Workflow

1. Inspect only enough to locate entry points, relevant instructions, acceptance criteria, and checks. Give Astra a compact handoff with absolute paths and concrete uncertainties, without secrets or full logs.
2. Spawn one read-only Astra advisor using `gpt-6-astra`, `high`, and no inherited conversation. Ask for an actionable plan, risks, and cheapest acceptance checks. Retain its ID.
3. Luna implements the plan, runs proportionate checks, and handles routine errors. If a patch misses context, reread the affected region and retry once minimally; do not replay stale broad patches.
4. Send the actual changed paths, scoped diff, observed checks, and remaining uncertainties to the same advisor. It must inspect the actual result and return `PASS`, `FIX_REQUIRED`, or `UNVERIFIED`.
5. For `FIX_REQUIRED`, allow one targeted Luna repair and one final verification by the same advisor. Stop after that and report remaining issues.

Use bounded waits, preserve authorization boundaries, and never claim measured savings without comparable token records. A reused planner is not an independent reviewer.
