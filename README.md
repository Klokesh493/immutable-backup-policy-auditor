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

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

A successful backup does not prove recovery controls are in place. Reviewers need to identify missing immutability, retention, encryption, and offsite copies.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 policy_auditor.py sample_policies.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
