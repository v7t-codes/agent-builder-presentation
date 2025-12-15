---
title: "Baselines & benchmarks (why scaffolding exists)"
status: "Draft"
---

# Baselines & benchmarks: why scaffolding exists

## Three regimes people conflate

| Regime | What it is | Typical failure mode | What builders sell |
| --- | --- | --- | --- |
| **Vanilla** | Strong model + a basic loop + tool calls | brittle edges, gets lost, high latency | baseline runtime + tool wiring |
| **Adapted (scaffolded)** | workflows + adapters + policies + eval gates | still fails, but within a controlled blast radius | governance, connectors, memory, evals, ops tooling |
| **Trained / RL** | learned policies beyond prompts | expensive; data + safety constraints | domain reliability where economics justify training |

## The baseline is moving fast (and will keep moving)

![](assets/diagrams/tau2_bench_tool_use.png)

**Interpretation:** baseline model capability is a moving target. What was “agentic” last year becomes “default” faster than most teams expect.

> **The bitter lesson (Sutton):** over time, general methods that scale with compute and data tend to win over hand-built domain tricks.  
> https://www.incompleteideas.net/IncIdeas/BitterLesson.html

![](assets/diagrams/osworld_verified_success_by_approach.png)

What this implies:

- On OSWorld (desktop), verified submissions show a large gap between “general models” and “agentic frameworks” — scaffolding and control layers materially change outcomes.
- As models improve, more workflows shift from “needs heavy scaffolding” → “works with light scaffolding”.
- Durable value shifts to **evals, governance, connectors, and feedback/training loops** (not prompt-heavy orchestration).
- Better models reduce *workflow complexity*, not the need for *control* in high-risk domains.

## End-to-end benchmarks (high signal)

| Benchmark | Surface | What it tests | Why it matters |
| --- | --- | --- | --- |
| **OSWorld** — https://os-world.github.io • paper: https://arxiv.org/abs/2404.07972 | Desktop | Full desktop control across apps | Closest public proxy for “office work” |
| **WebArena** — https://arxiv.org/abs/2307.13854 | Browser | Web navigation + task completion | Many enterprises are “web portals with bad APIs” |
| **WebChoreArena** — https://arxiv.org/abs/2506.01952 | Browser | Long-horizon chores (memory + bookkeeping) | Stress test for real-world failure modes |
| **GAIA** — example writeup: https://h2o.ai/blog/2024/h2o-ai-tops-gaia-leaderboard/ | Multi-tool | Browse, read, calculate, use tools | “Power user assistant” proxy |
| **τ-bench** — repo: https://github.com/sierra-research/tau-bench | Tool + state | Stateful tool calls + policy constraints | Forces governance-like behavior |
| **TheAgentCompany** — writeup: https://jilltxt.net/llms-fail-at-70-of-simple-office-tasks/ | Multi-surface | Coordination + realistic multi-step work | Checks “company in a box” narratives |

## One number that captures the gap

WebChoreArena authors show a sharp drop on long-horizon web chores; in one setup, GPT‑4o is reported at **6.8%**.  
OpenReview PDF: https://openreview.net/pdf/679e1c2a0295a7f380d7fabd0d64b199a48efad6.pdf

## Practical takeaway

Baseline agents are a floor. Production reliability still comes from:

- workflow scaffolding + adapter depth
- eval gates + regression control
- permissions, approvals, and auditability
