# Benchmark

This file is updated only from comparable runs. The baseline is **pure Astra** completing the same task from the same compact prompt. The treatment is the **Astra-Luna workflow**: Astra plan, Luna execution, and the same Astra advisor verifying the result.

Do not compare this workflow to Luna-only and call that an Astra saving. Do not report a percentage until both runs expose comparable input/output/total token records and pass the same acceptance checks.

## Protocol

1. Use a small deterministic coding task with identical files, prompt, and acceptance tests.
2. Run it once as pure `gpt-6-astra` with `high` reasoning.
3. Reset the fixture and run it through `gpt-6-astra` planning, `gpt-5.6-luna` execution, and the same Astra advisor's verification.
4. Sum model token usage for all calls in each run. Report input, output, reasoning, cached input, total, and wall time when available.
5. Record failures, retries, tool availability, and whether the result passed the same tests.

## Result: 2026-09-15 smoke benchmark

Fixture: `priority.py` plus four focused `unittest` cases. Both variants passed all four tests.

| Variant | Role calls | Observable total tokens | Evidence |
|---|---:|---:|---|
| Pure Astra | 1 | `91,207` | session token usage record |
| Astra-Luna | 3 roles; 2 records exposed | `>=596,309` | Astra advisor `254,604` + Luna repair `341,705`; initial Luna record unavailable |

This tiny task did **not** save tokens. The observed lower bound is at least `6.54x` the pure-Astra run, or `-553.8%` relative savings, before counting the missing initial Luna executor record. That is orchestration overhead, not a failure of the intended large-task economics: a four-test edit is too small to amortize planning and verification. It is also why this project does not advertise a fixed savings percentage.

The benchmark is reproducible from the fixture and the recorded session files, but the Astra-Luna number is a lower bound because the desktop export did not expose the initial Luna executor's independent token record. Larger multi-file tasks with long execution loops are the intended target; measure them with the same protocol before making a savings claim.

The Goal aggregate usage snapshot at the end of the benchmark preparation was `173,823` tokens. It includes repository preparation, orchestration, tool calls, and this report, so it must not be treated as either variant's token total.
