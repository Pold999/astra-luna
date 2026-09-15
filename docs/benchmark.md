# Benchmark

This file is updated only from comparable runs. The baseline is **pure Astra** completing the same task from the same compact prompt. The treatment is the **Astra-Luna workflow**: Astra plan, Luna execution, and the same Astra advisor verifying the result.

Do not compare this workflow to Luna-only and call that an Astra saving. Do not report a percentage until both runs expose comparable input/output/total token records and pass the same acceptance checks.

## Protocol

1. Use a small deterministic coding task with identical files, prompt, and acceptance tests.
2. Run it once as pure `gpt-6-astra` with `high` reasoning.
3. Reset the fixture and run it through `gpt-6-astra` planning, `gpt-5.6-luna` execution, and the same Astra advisor's verification.
4. Sum model token usage for all calls in each run. Report input, output, reasoning, cached input, total, and wall time when available.
5. Record failures, retries, tool availability, and whether the result passed the same tests.

Before measuring the full pipeline, run routing controls: a one-file mechanical edit should report `direct Luna fast path` and create no Astra advisor; a cross-file design task should create one reusable advisor. This prevents the benchmark harness from accidentally overriding the production fast path.

## Reporting guidance

Use the protocol above to measure comparable pure-Astra and Astra-Luna runs on a substantive task. Report input, output, reasoning, cached input, total tokens, wall time, acceptance results, and any missing telemetry. Do not publish a fixed savings percentage from a single smoke task; use several representative tasks before making a generalized claim.

The included fixture and focused tests provide a quick installation check. They are intentionally separate from any generalized efficiency claim because planning and verification overhead depends strongly on task size.
