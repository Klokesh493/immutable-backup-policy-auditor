# Immutable Backup Policy Auditor architecture

Audits backup policies for immutability, retention, encryption, and offsite copy coverage.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
