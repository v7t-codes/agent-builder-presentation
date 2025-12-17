---
title: "Premise: Agent kernel + scaffolding"
status: "Draft"
---

# Premise: agent kernels are the unit

An “agent” is not just a model call. It’s an **agent kernel** wrapped in scaffolding that makes it safe and reliable in the real world.

> **LLM‑OS frame:** in a world of “LLM‑OS,” **agents are the new apps** — the “app” is a goal-driven loop plus the scaffolding around it.

## The agent kernel — invariant

- The control loop runs goal → plan → act → update state → repeat.
- An LLM or other policy chooses the next step and tool call.
- A tool executor runs calls, retries failures, and decides when to stop.
- State includes a scratchpad and checkpoints so work can resume after failure.
- A learning loop turns logs into evals, labeled data, and updates: prompts, policies, and fine‑tuning.

## The scaffolding — where products differentiate

- Context assembly pulls retrieval, memory, and tool/policy context into the run.
- Tool adapters and connectors translate intent into safe actions in real systems.
- Governance enforces permissions, approvals, and auditability.
- Observability and eval gates make failures debuggable and prevent regressions.
- Environment control manages browser/desktop sessions, replays, and long‑lived authentication.

**Market thesis:** most “agent builders” are selling a different slice of this scaffolding.

## Diagram: kernel + scaffolding

![](assets/diagrams/agent_kernel_scaffolding.svg)
