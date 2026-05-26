# Strands-Core

## Purpose

Strands-Core is the foundational orchestration agent for the AI Stack project.

Its purpose is to provide:

* Token-conscious agent orchestration
* Explicit and inspectable tool execution
* LiteLLM-based provider abstraction
* Transparent resource accounting
* Modular long-term architecture
* Local-first operation where practical
* Future-compatible multi-agent infrastructure

This project intentionally rejects opaque "magic agent" architecture patterns that generate uncontrolled token burn and hidden reasoning overhead.

---

## Design Philosophy

Strands-Core prioritizes:

1. Transparency over abstraction
2. Explicit control over hidden autonomy
3. Modular composition over monolithic frameworks
4. Budget awareness over maximal capability
5. Replaceable components over ecosystem lock-in
6. Measured scalability over hype-driven complexity

---

## Core Constraints

The agent must:

* Log all major tool invocations
* Support token/resource accounting
* Avoid uncontrolled recursive loops
* Allow configurable approval gates
* Support aggressive context compression
* Remain provider-agnostic through LiteLLM
* Be inspectable and debuggable at runtime

---

## Non-Goals

This project is NOT attempting to:

* Build an unrestricted autonomous agent
* Maximize benchmark scores at any cost
* Depend on a single provider ecosystem
* Hide orchestration behavior from the user
* Optimize for social-media-style demos

---

## Long-Term Vision

Strands-Core is intended to evolve into a modular orchestration substrate capable of supporting:

* Multiple interchangeable agent frameworks
* Shared memory infrastructure
* Shared telemetry infrastructure
* Shared tool registries
* Dynamic capability loading
* Lightweight specialized subagents
* Budget-aware scaling policies
* Future local model integration

---

## Current Status

Phase: Foundation

Current priorities:

* Repository architecture
* LiteLLM integration
* Token/resource observability
* Minimal operational agent loop
* Controlled tool execution
* Future dashboard integration

No uncontrolled autonomy will be introduced during early phases.
