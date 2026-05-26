# Strands-Core System Architecture

## Architectural Intent

Strands-Core is designed as a lightweight, budget-aware orchestration substrate for modular AI agents.

The system prioritizes:

- explicit control,
- transparent execution,
- measurable resource consumption,
- modular extensibility,
- and future portability across models and frameworks.

The architecture intentionally avoids:

- permanently-loaded massive tool registries,
- uncontrolled recursive autonomy,
- opaque internal reasoning layers,
- and provider lock-in.

Strands-Core treats autonomy as an earned capability that scales only when justified by available resources, observability, and user-defined policy constraints.

---

## Primary Design Objectives

1. Maintain strict visibility into token and resource usage
2. Support modular agent and tool composition
3. Enable future multi-agent orchestration
4. Preserve provider independence through LiteLLM abstraction
5. Support aggressive context management and compression
6. Allow configurable autonomy escalation policies
7. Keep all critical runtime behavior inspectable and debuggable

---

## Core Runtime Topology

Strands-Core is organized into a small number of explicit runtime layers.

Initial architecture:

```text
User
  ↓
Strands-Core Orchestrator
  ↓
Policy / Budget Layer
  ↓
LiteLLM Gateway
  ↓
Selected Model Provider

```

Optional future layers:

```text
Subagents
Memory Services
Tool Registry
Telemetry Dashboard
Local Model Runtime
Task Queue System
Workflow Engine
```

---

## Runtime Layer Responsibilities

### 1. Orchestrator Layer

Responsible for:

- task interpretation,
- execution planning,
- tool selection,
- approval handling,
- and coordination of downstream systems.

The orchestrator should remain lightweight and avoid excessive embedded logic.

---

### 2. Policy / Budget Layer

Responsible for enforcing:

- token budgets,
- recursion limits,
- autonomy constraints,
- approval requirements,
- model routing policies,
- and execution safety controls.

This layer acts as a governance boundary between user intent and autonomous execution.

No downstream component should bypass this layer.

---

### 3. LiteLLM Gateway Layer

Responsible for:

- provider abstraction,
- model routing,
- fallback handling,
- centralized configuration,
- telemetry collection,
- and future cost accounting integration.

LiteLLM serves as the provider isolation boundary for the system.

---

### 4. Model Provider Layer

Represents external or local inference providers.

Examples include:

- OpenAI,
- Anthropic,
- Gemini,
- Groq,
- Ollama,
- vLLM,
- llama.cpp,
- or future local inference runtimes.

The architecture intentionally treats providers as interchangeable infrastructure components.

---

## Autonomy Escalation Model

Strands-Core operates using graduated autonomy tiers rather than unrestricted autonomous execution.

The system defaults to the lowest-cost execution strategy capable of completing a task successfully.

Higher-cost reasoning and orchestration behaviors must be explicitly triggered by:

- user approval,
- policy configuration,
- task complexity thresholds,
- or failure recovery conditions.

---

### Tier 0 — Direct Execution

Characteristics:

- single-pass execution,
- minimal reasoning,
- no recursive planning,
- no delegated subagents,
- lowest token consumption.

Use cases:

- simple commands,
- direct tool invocation,
- information retrieval,
- lightweight automation tasks.

---

### Tier 1 — Assisted Orchestration

Characteristics:

- short-horizon planning,
- limited tool chaining,
- bounded memory usage,
- constrained retries,
- explicit execution visibility.

Use cases:

- structured workflows,
- multi-step automation,
- controlled browser or filesystem tasks.

---

### Tier 2 — Managed Autonomy

Characteristics:

- delegated subagents,
- adaptive planning,
- memory-assisted execution,
- dynamic tool selection,
- bounded recursive reasoning.

Requires:

- elevated policy permissions,
- active telemetry,
- strict token accounting,
- and runtime safeguards.

---

### Tier 3 — Experimental Extended Autonomy

Characteristics:

- long-running workflows,
- persistent task execution,
- background orchestration,
- dynamic workflow generation,
- and self-directed task decomposition.

This tier is considered experimental and should remain disabled by default until observability and governance systems are mature.

---

## Escalation Principles

The system should always prefer:

1. lower-cost execution,
2. fewer reasoning passes,
3. smaller active context windows,
4. specialized lightweight tools,
5. and deterministic workflows where possible.

Escalation to higher autonomy tiers should occur only when lower tiers fail or task complexity demonstrably requires additional orchestration capability.

---

