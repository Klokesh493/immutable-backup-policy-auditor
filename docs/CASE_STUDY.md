# Immutable Backup Policy Auditor walkthrough

## Business problem

Audits backup policies for immutability, retention, encryption, and offsite copy coverage.

## Reproduce the workflow

Run `python3 policy_auditor.py sample_policies.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
prod-db: pass
dev-share: immutable,offsite_copy,retention_days
```

The sample supplies these fields. `policy`, `immutable`, `encrypted`, `offsite_copy`, `retention_days`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
