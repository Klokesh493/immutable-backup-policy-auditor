# Immutable Backup Policy Auditor architecture

Audits backup policies for immutability, retention, encryption, and offsite copy coverage.

```mermaid
flowchart LR
    N0["sample_policies.csv"]
    N1["policy_auditor.py"]
    N2["audit"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
