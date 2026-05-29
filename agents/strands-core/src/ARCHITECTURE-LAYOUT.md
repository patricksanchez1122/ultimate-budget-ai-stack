# Runtime Architecture Layout

## Purpose

This document defines the high-level runtime structure of Strands-Core.

Its purpose is to preserve:

- subsystem boundaries,
- dependency direction,
- orchestration responsibilities,
- and long-term architectural coherence as the system evolves.

This file acts as the initial nervous system map for the runtime body.

---

## Core Runtime Structure

```text
src/
|-- orchestrator/
|-- policy/
|-- telemetry/
|-- providers/
|-- tools/
`-- memory/

```