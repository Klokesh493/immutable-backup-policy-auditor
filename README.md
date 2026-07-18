# Immutable Backup Policy Auditor

Audits backup policies for immutability, retention, encryption, and offsite copy coverage.

Focus: Backup-platform DevSecOps controls.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 policy_auditor.py sample_policies.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
