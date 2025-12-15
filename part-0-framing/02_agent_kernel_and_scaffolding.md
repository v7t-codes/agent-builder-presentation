---
title: "Premise: Agent kernel + scaffolding"
status: "Draft"
---

# Premise: agent kernels are the unit

An “agent” is not just a model call. It’s an **agent kernel** wrapped in scaffolding that makes it safe and reliable in the real world.

## The agent kernel (invariant)

- Control loop: goal → plan → act → update state → repeat
- Action selection: an LLM (or policy) chooses the next step/tool call
- Execution: tool runner, retries, and termination logic
- State: scratchpad + checkpoints (so work can resume after failure)
- Learning loop: logs → evals → labeled data → updates (prompts/policies/finetune)

## The scaffolding (variable, where products differentiate)

- Context assembly (retrieval + memory + tool/policy context)
- Tool adapters + connectors into real systems
- Permissions, approvals, and audit (governance)
- Observability + eval gates (debuggability + regression control)
- Environment control (browser/desktop sessions, replays, long‑lived auth)

**Market thesis:** most “agent builders” are selling a different slice of this scaffolding.

## Diagram: kernel + scaffolding

![](assets/diagrams/agent_kernel_scaffolding.png)
