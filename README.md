# Immutable Backup Policy Auditor

A successful backup does not prove recovery controls are in place. Reviewers need to identify missing immutability, retention, encryption, and offsite copies.

## What I built

I built a policy audit that checks immutability, encryption, offsite copies, and a minimum 30-day retention period. Its output lists every failing control by policy name.

## How it works

```mermaid
flowchart LR
    A["Backup policy CSV"]
    B["Check protection flags and minimum 30-day retention"]
    C{"Any control missing?"}
    D["List policy gaps"]
    E["No gaps"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [policy_auditor.py](policy_auditor.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 policy_auditor.py sample_policies.csv
```

Prod DB passes. Dev share lacks immutability, an offsite copy, and sufficient retention. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 policy_auditor.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

Policy declarations need to be reconciled with actual storage configuration and restore evidence.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
