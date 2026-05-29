# Copy-Paste Workflow Governance

## Purpose

This document defines the operational workflow used for human-AI repository collaboration within the project.

The workflow exists to preserve:

* execution continuity,
* operational reliability,
* verification discipline,
* repository integrity,
* recoverability,
* and long-horizon collaboration efficiency.

The workflow treats continuity preservation as operational infrastructure rather than informal habit.

---

## Core Principle

Work that is not verified should be treated as incomplete.

Human-AI collaboration introduces opportunities for:

* context drift,
* execution drift,
* workflow interruption,
* copy-paste errors,
* file ambiguity,
* and repository inconsistency.

Therefore:

all operational work should follow explicit verification checkpoints.

Verification precedes trust.

---

## Workflow Resurrection Principle

Sessions may be interrupted by:

* context limits,
* provider changes,
* runtime failures,
* operator interruptions,
* infrastructure failures,
* or conversational drift.

To restore workflow continuity, the project adopts:

```text
RW
```

RW means:

```text
Resurrect Workflow
```

RW instructs participants to restore the established operational workflow before continuing implementation work.

RW restores process before action.

---

## Standard Content Workflow

The preferred content creation workflow is:

1. identify target file,
2. create file if necessary,
3. generate content,
4. paste content into file,
5. verify file contents,
6. evaluate correctness,
7. commit changes,
8. push changes,
9. continue implementation.

Content generation should occur before commit operations.

Verification should occur before git operations.

---

## Verification Requirement

All newly created files should be verified using:

```powershell
Get-Content <file>
```

Verification ensures:

* content exists,
* content was saved,
* formatting survived editing,
* and the intended document was modified.

File existence alone is not sufficient verification.

---

## Directory Validation

Before file operations occur, the current working directory should be confirmed.

Example:

```powershell
pwd
```

or

```powershell
Get-Location
```

This prevents accidental operations inside incorrect locations such as:

```text
C:\Windows\System32
```

instead of:

```text
C:\Users\RT\ai-stack
```

Directory validation reduces continuity errors.

---

## Copy-Paste Integrity Principle

Generated content should remain visible in the conversation before editing begins.

The workflow should avoid:

* placeholder creation without content,
* invisible editing assumptions,
* unverified file population,
* or skipped verification steps.

Copy-paste operations should remain observable.

---

## Git Checkpoint Discipline

Git commits represent continuity checkpoints.

Preferred sequence:

1. verify content,
2. evaluate correctness,
3. git add,
4. git commit,
5. git push.

Repository history should record validated state rather than assumed state.

---

## Migration Workflow

Repository restructuring should follow:

1. evaluate topology,
2. define migration target,
3. create destination,
4. migrate incrementally,
5. verify moved files,
6. verify references,
7. commit,
8. push.

Migration without verification increases continuity risk.

---

## Failure Recovery

When workflow failure occurs:

* stop implementation,
* identify last verified checkpoint,
* restore continuity,
* verify repository state,
* resume execution.

Recovery should prioritize correctness over speed.

---

## Human-AI Collaboration Principle

The workflow exists to support durable collaboration between:

* humans,
* AI systems,
* and future contributors.

Operational discipline improves:

* recoverability,
* continuity restoration,
* repository integrity,
* onboarding,
* and long-term maintainability.

The workflow should survive interruptions without losing coherence.

---

## Architectural Role

Within the Immortal Evolving Body philosophy, the copy-paste workflow functions as:

* continuity protocol,
* operational coordination layer,
* verification discipline,
* and collaboration infrastructure.

The workflow preserves reliable execution across evolving sessions.

---

## Long-Term Intent

The long-term goal of the copy-paste workflow is to support:

* reliable collaboration,
* recoverable execution,
* repository integrity,
* verification-first development,
* and long-horizon operational continuity.

The workflow should evolve without sacrificing:

* observability,
* recoverability,
* correctness,
* continuity,
* or operator visibility.

The workflow survives interruption.

Verification preserves continuity.

Execution follows discipline.

---
