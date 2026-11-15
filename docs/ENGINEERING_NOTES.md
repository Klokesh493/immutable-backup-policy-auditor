# Skills and verification

## What this repository demonstrates

A policy audit that checks immutability, encryption, offsite copies, and a minimum 30-day retention period. Its output lists every failing control by policy name.

## Reproduce the result

Prod DB passes. Dev share lacks immutability, an offsite copy, and sufficient retention. Reproduce the primary fixture with `python3 policy_auditor.py sample_policies.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

Policy declarations need to be reconciled with actual storage configuration and restore evidence.

Use reported control gaps to review the actual backup policy with its owner. A policy export does not demonstrate that restore works.

[policy_auditor.py](../policy_auditor.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
