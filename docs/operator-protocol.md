# Operator Protocol

## Purpose

This document defines the operational collaboration model used during development of Strands-Core.

Its purpose is to preserve:

- architectural continuity,
- implementation discipline,
- verification rigor,
- and long-term project coherence across sessions, contributors, and models.

This file should be treated as persistent operational context for future development work.

---

## Core Development Philosophy

Strands-Core is developed using:

- incremental implementation,
- explicit verification,
- architecture-first reasoning,
- and budget-conscious engineering practices.

The project intentionally prioritizes:

1. clarity over speed,
2. inspectability over abstraction,
3. modularity over monolithic design,
4. controlled autonomy over unrestricted agency,
5. and long-term maintainability over rapid feature accumulation.

---

## Verification Discipline

No major operation should be assumed successful without verification.

Development workflow should follow:

1. execute action,
2. verify result,
3. inspect state,
4. correct inconsistencies,
5. then proceed incrementally.

This applies to:

- filesystem operations,
- runtime behavior,
- dependency installation,
- orchestration logic,
- memory systems,
- and autonomous workflows.

---

## Anti-Assumption Policy

The system should avoid:

- assuming file existence,
- assuming successful writes,
- assuming runtime state,
- assuming dependency integrity,
- or assuming architectural correctness without inspection.

Verification is mandatory.

---

## Context Preservation Principles

Project continuity should rely primarily on repository documentation rather than conversational memory alone.

Critical architectural decisions should be documented explicitly within the repository.

Important reasoning, constraints, and design philosophy should remain recoverable from repository state.

---

## Long-Term Architectural Direction

Strands-Core is intended to evolve gradually toward:

- modular orchestration,
- scalable autonomy,
- shared telemetry infrastructure,
- memory-aware execution,
- lightweight subagent systems,
- and future local-first AI operation.

However:

all capability expansion must remain subordinate to:

- budget governance,
- observability,
- runtime safety,
- and operator control.

---

## Preferred Development Methodology

Preferred workflow:

- small reversible steps,
- immediate verification,
- architecture before implementation,
- constrained experimentation,
- and progressive capability escalation.

Large uncontrolled implementation jumps should be avoided.

---

## Operational Priority Order

When tradeoffs occur, prioritize:

1. runtime stability,
2. budget control,
3. observability,
4. modularity,
5. portability,
6. autonomy,
7. performance optimization.

---

## Repository Role

This repository functions as:

- source control,
- architecture memory,
- operational continuity layer,
- implementation history,
- and governance reference.

The repository is considered part of the system architecture itself.

---