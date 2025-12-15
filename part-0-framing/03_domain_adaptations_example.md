---
title: "Agents today are adaptations of the same kernel"
status: "Draft"
---

# Agents today are adaptations of the same kernel

## The pattern

- The kernel stays the same: goal → plan → act → update state → loop.
- The scaffolding changes by domain: **surface, tools, memory, policies, evals**.

## Clear example: “Refund + customer support” agent

- **Surface:** Helpdesk + payments APIs; sometimes browser for edge-case portals
- **Tools:** Zendesk/Jira, Stripe, CRM, internal policy service, knowledge base
- **Policies:** approval thresholds, PII handling, audit logs, safe rollback
- **Memory:** ticket history, prior refunds, customer tier/context
- **Evals:** policy compliance + refund correctness + deflection + CSAT

## What gets heavier in other domains (at a glance)

| Domain | Surface | What gets heavier |
| --- | --- | --- |
| IT / employee support | API + internal tools | RBAC/approvals + incident safety |
| Finance ops | API + documents | provenance + reconciliation + human review |
| Browser/desktop automation | browser/desktop | sessions + replays + breakage handling |

## Adaptation is not a one-time setup (continual learning)

The best teams treat “domain adaptation” as a loop:

1) **Instrument** runs (traces, tool calls, outcomes, human overrides)
2) **Evaluate** against domain metrics (correctness, policy compliance, time/cost, escalation rate)
3) **Create data** from failures + edge cases (curate, label, synthesize)
4) **Update** the system (prompts, policies, adapters, and when justified: fine‑tune/RL)

This is how kernels turn “usage” into compounding reliability.

## Takeaway

“Agents” look different because the **scaffolding** is different — and scaffolding intensity is primarily set by **surface + risk**.
