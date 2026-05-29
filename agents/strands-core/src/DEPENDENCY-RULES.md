# Dependency Rules

## Purpose

This document defines mandatory dependency and communication rules for Strands-Core runtime components.

Its purpose is to preserve:

- architectural coherence,
- subsystem isolation,
- governance integrity,
- observability,
- and long-term maintainability.

These rules exist to prevent uncontrolled coupling and architecture drift as the system evolves.

---

## Core Principle

All runtime communication must follow explicit, inspectable dependency direction.

Subsystems should communicate through controlled interfaces rather than unrestricted cross-layer access.

No subsystem should gain implicit authority through accidental coupling.

---

## Runtime Dependency Hierarchy

```text
User
  |
  v
Orchestrator
  |
  v
Policy
  |
  v
Providers
  |
  v
Models
```

Supporting systems:

```text
Telemetry  -> passive observation only
Memory     -> contextual support only
Tools      -> explicit invocation only
```

---

## Authority Boundaries

### 1. Orchestrator Authority

The orchestrator may:

- coordinate workflows,
- request policy evaluation,
- invoke tools through approved pathways,
- query memory systems,
- and communicate with provider interfaces.

The orchestrator may NOT:

- bypass policy validation,
- directly override governance constraints,
- or mutate runtime policy state without authorization.

---

### 2. Policy Layer Authority

The policy layer acts as the governance boundary of the system.

Policy systems may:

- approve or deny execution,
- enforce token limits,
- restrict recursion,
- control autonomy escalation,
- validate provider usage,
- and enforce runtime safeguards.

No downstream system may bypass policy validation.

---

### 3. Provider Layer Constraints

Provider systems are infrastructure adapters only.

Providers may:

- route inference requests,
- manage provider-specific configuration,
- handle retries and failover,
- and collect provider telemetry.

Providers may NOT:

- autonomously invoke tools,
- modify orchestration behavior,
- bypass policy systems,
- or directly alter memory state.

---

### 4. Tool Execution Constraints

Tools are capability extensions, not autonomous actors.

Tools must only execute through explicit orchestrator-approved pathways.

Tools may NOT:

- self-invoke recursively,
- escalate autonomy independently,
- mutate governance systems,
- or directly control providers.

---

### 5. Memory System Constraints

Memory systems exist to support continuity and contextual retrieval.

Memory systems may:

- store context,
- retrieve prior state,
- assist compression,
- and support continuity recovery.

Memory systems may NOT:

- autonomously execute workflows,
- bypass orchestration,
- invoke tools independently,
- or mutate governance state.

---

### 6. Telemetry Constraints

Telemetry systems are observational infrastructure only.

Telemetry may:

- record execution state,
- collect metrics,
- track budgets,
- and support debugging.

Telemetry must remain passive.

Telemetry systems may NOT:

- alter execution behavior,
- invoke workflows,
- or mutate orchestration state.

---

## Dependency Direction Rules

Allowed dependency direction:

```text
orchestrator
    |
    v
policy
    |
    v
providers
```

Supporting systems:

```text
orchestrator -> tools
orchestrator -> memory
orchestrator -> telemetry
policy -> telemetry
providers -> telemetry
```

Disallowed dependency examples:

```text
tools -> policy
tools -> providers
memory -> tools
providers -> orchestrator
telemetry -> orchestration control
```

---

## Circular Dependency Prevention

Subsystems should avoid circular runtime dependencies wherever possible.

Bidirectional orchestration relationships should require explicit architectural justification and documentation.

Implicit cyclical orchestration behavior is prohibited.

---

## Architectural Escalation Principle

Higher-authority systems may coordinate lower-authority systems.

Lower-authority systems must not silently acquire control over higher-authority systems.

Governance direction must remain explicit and inspectable.

---

## Long-Term Intent

These dependency rules exist to preserve:

- modular evolution,
- replaceable cognitive engines,
- governance integrity,
- runtime observability,
- and controlled autonomy expansion over long operational timelines.

Architecture drift should be treated as a system health issue rather than a cosmetic concern.

---