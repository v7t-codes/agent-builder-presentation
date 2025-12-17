---
title: "Agents today are adaptations of the same kernel"
status: "Draft"
---

# Agents today are adaptations of the same kernel

## The pattern

- The kernel stays the same: goal → plan → act → update state → loop.
- The scaffolding changes by domain: **surface, tools, memory, policies, evals**.

## Clear example: “Refund + customer support” agent

- **Surface:** The surface is helpdesk and payments APIs, with a browser fallback for edge‑case portals.
- **Tools:** The tool set is typically Zendesk/Jira, Stripe, a CRM, an internal policy service, and a knowledge base.
- **Policies:** The policy layer enforces approval thresholds, PII handling, audit logs, and safe rollback behavior.
- **Memory:** The memory layer includes ticket history, prior refunds, and customer tier/context.
- **Evals:** The eval harness measures policy compliance, refund correctness, deflection, and CSAT.

![](assets/diagrams/customer_support_agent_scaffolding.png)

## What gets heavier by domain

| Domain | Surface | What gets heavier |
| --- | --- | --- |
| IT / employee support | API + internal tools | RBAC/approvals + incident safety |
| Finance ops | API + documents | provenance + reconciliation + human review |
| Browser/desktop automation | browser/desktop | sessions + replays + breakage handling |

## Adaptation is continual

The best teams treat “domain adaptation” as a loop:

1) **Instrument** runs: traces, tool calls, outcomes, human overrides
2) **Evaluate** against domain metrics: correctness, policy compliance, time/cost, escalation rate
3) **Create data** from failures + edge cases: curate, label, synthesize
4) **Update** the system: prompts, policies, adapters, and when justified, fine‑tune/RL

This is how kernels turn “usage” into compounding reliability.

## Takeaway

“Agents” look different because the **scaffolding** is different — and scaffolding intensity is primarily set by **surface + risk**.
