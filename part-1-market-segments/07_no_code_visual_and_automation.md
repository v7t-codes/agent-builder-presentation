---
title: "Company Type 2: No-code & visual — incl. automation subset"
status: "Updated v2 — no-code/visual only + hypotheses"
---

# Company type 2: No-code & visual AI agent / workflow designers

This category covers products where the **primary agent-building surface is a UI** — canvas/flow/studio — not a developer SDK.

It also includes a critical subset: **automation platforms** like RPA / iPaaS / workflow evolving into agent builders by adding LLM/agentic steps + guardrails.

## Segment definition

- They serve business and ops teams that want to prototype workflows quickly in a UI.
- They serve IT and engineering teams that need governance, connectors, and a production finish path.

## What they build

- They build visual agent and workflow designers: canvas/studio.
- They ship connector libraries and action templates.
- They provide execution infrastructure: runs, logs, approvals, evals, packaged behind a UI.

## Validation bar

A company is included only if, on its own product pages/docs, it is clearly positioned as at least one of:

- It is a **visual agent or workflow builder**: canvas/graph/studio.
- It is a **suite-embedded agent builder** inside a larger enterprise suite.
- It is an **automation platform** adding explicit agentic steps and builder UX.

We deliberately do *not* include “chat-with-your-data” point products unless there is a real workflow/agent designer.

**Validated companies in this type: 52**

## Subsegments

### A) Standalone no-code / visual agent builders — UI-first

These are **standalone** UI-first builders — commercial or open-source — where the core product is “build an agent / workflow in a canvas.”

| Company | Subsegment tags | Surface | Primary link | Notes |
| --- | --- | --- | --- | --- |
| Lindy.ai | ui:horizontal | API | https://www.lindy.ai | AI assistant / agent workflows; UI-led. |
| Adopt AI Agent Builder | ui:horizontal | API | https://www.adopt.ai/product/agent-builder | UI builder for agents and workflows. |
| Ag.dev | ui:horizontal | API | https://ag.dev | UI-first agent building surface. |
| Stack AI | ui:horizontal, ui:enterprise | API | https://www.stack-ai.com | Workflow/agent builder targeting teams. |
| Hypermindz Agentic Platform | ui:horizontal | API | https://www.hypermindz.ai/discover-platform | Agentic platform with a UI-led build surface. |
| Flowise | ui:open_source, ui:canvas, acquired | API | https://flowiseai.com | Open-source LLM flow builder; now part of Workday. |
| Langflow | ui:open_source, ui:canvas | API | https://www.langflow.org | Open-source visual flow builder for LLM apps/agents. |
| Dify | ui:open_source, ui:enterprise | API | https://dify.ai | UI-first builder for AI apps/agents. |
| Relevance AI | ui:horizontal | API | https://relevanceai.com | Visual agent builder / workflows. |
| Dust | ui:enterprise | API | https://dust.tt | Enterprise agent building + deployment in a UI. |
| Beam AI | ui:horizontal | API | https://beam.ai | Agentic automation builder surface. |
| Dynamiq | ui:horizontal | API | https://www.getdynamiq.ai/product/agents | Visual builder for agentic workflows. |
| Nainovate GenX | ui:enterprise | API | https://www.nainovate.ai/platform/development-tools/ | Enterprise-oriented agent building tooling. |
| Gumloop | ui:horizontal | API | https://www.gumloop.com | Visual workflow builder with AI steps. |
| Den — GetDen | ui:horizontal | API | https://getden.io | UI-first agent/workflow builder. |
| AgenticScale.AI Agent Builder | ui:horizontal | API | https://www.agenticscale.ai/agent-builder | Agent builder with UI-led design. |
| Writer — Writer.com | ui:enterprise, suite_like | API | https://www.writer.com | Enterprise platform with workflow/agent-like building blocks. |
| Jinba | ui:chat_to_workflow, ui:manifest | API | https://jinba.io | “Build through chat,” edit manifests visually, deploy workflows as APIs/MCP. |
| SmythOS Agent Studio | ui:agent_studio, ui:enterprise | API | https://smythos.com/product/agent-studio/ | Agent Studio UX for building and running agents. |
| MindStudio — YouAI | ui:horizontal | API | https://www.mindstudio.ai/ | No-code platform for building AI agents and workflows. |
| Vellum | ui:enterprise, ui:builder | API | https://www.vellum.ai | UI-led agent/workflow builder plus evaluation/ops tooling. |
| Rivet | ui:open_source, ui:desktop | Multi | https://rivet.ironcladapp.com/ | Open-source visual environment for building LLM prompt graphs/agents. |
| Botpress | ui:agent_studio, ui:chat | API | https://botpress.com/ | Agent Studio for building and deploying agents/bots. |
| Voiceflow | ui:voice, ui:chat | Voice | https://www.voiceflow.com | Visual builder for conversational/voice agents. |

### B) Suite-embedded builders — inside a larger suite / platform

These builders live **inside** a broader enterprise suite or low-code platform. They win on distribution + access to systems-of-record.

| Company | Subsegment tags | Surface | Primary link | Notes |
| --- | --- | --- | --- | --- |
| Microsoft Copilot Studio | suite:Microsoft, suite_embedded | Multi | https://copilotstudio.microsoft.com | Low-code studio for building/configuring copilots/agents in the Microsoft ecosystem. |
| Salesforce Agentforce | suite:Salesforce, suite_embedded | API | https://www.salesforce.com/agentforce/agent-builder/ | Builder surface embedded in Salesforce for CRM workflows. |
| Regrello — from Salesforce | suite:Salesforce, vertical_ops | API | https://www.regrello.com/ | Ops workflow automation product from Salesforce; positioned around agentic execution in business processes. |
| Oracle AI Agent Studio — Fusion AI | suite:Oracle, suite_embedded | API | https://docs.oracle.com/en/cloud/saas/fusion-ai/aiaas/overview.html | Embedded agent studio in Oracle Fusion ecosystem. |
| ServiceNow AI Agent Studio | suite:ServiceNow, suite_embedded | Multi | https://www.servicenow.com/products/ai-agents.html | Agent Studio / AI agents within the Now Platform. |
| SAP Joule Studio | suite:SAP, suite_embedded | Multi | https://help.sap.com/docs/joule-studio | Studio to build/customize Joule agents in SAP Build / SAP apps. |
| HubSpot Breeze Agents / Studio | suite:HubSpot, suite_embedded | API | https://www.hubspot.com/products/artificial-intelligence | Breeze agents embedded in HubSpot; configurable agent experiences. |
| Atlassian Rovo Studio | suite:Atlassian, suite_embedded | Multi | https://support.atlassian.com/rovo/docs/studio/ | Studio for building Rovo agents/automations in Atlassian cloud. |
| Zoho Zia Agent Studio | suite:Zoho, suite_embedded | Multi | https://www.zoho.com/zia/ | Zoho’s agent studio concept inside the Zoho suite — “Zia Agents”. |
| Freshworks AI Agent Studio | suite:Freshworks, suite_embedded | Multi | https://www.freshworks.com/freshdesk/omni/freddy-ai-automation/ | No-code agent builder inside Freshworks products. |
| Zendesk AI Agent Builder | suite:Zendesk, suite_embedded, support_domain | Multi | https://support.zendesk.com/hc/en-us/articles/5352026794010-About-automated-resolutions-for-AI-agents | Builder surface for AI agents inside Zendesk. |
| Hyland AI Agent Builder | suite:Hyland, suite_embedded | API | https://www.hyland.com/en/solutions/products/hyland-agent-builder | Embedded builder for content/process workflows inside Hyland. |
| Alation Agent Studio | suite:Alation, suite_embedded | API | https://www.alation.com/product/agent-studio/ | Agent Studio embedded in Alation’s data catalog platform. |
| OutSystems Agent Workbench | low_code_platform, suite_embedded | Multi | https://www.outsystems.com/low-code-platform/agentic-ai-workbench/ | Low-code app platform adding an agent workbench. |

### C) Automation platforms evolving into agent builders — RPA / iPaaS / workflow

These are workflow automation vendors adding agentic steps. They often win via existing connector libraries, governance, and enterprise sales motion.

| Company | Subsegment tags | Surface | Primary link | Notes |
| --- | --- | --- | --- | --- |
| UiPath Agent Builder | automation:rpa, incumbent | Multi | https://www.uipath.com/product/agent-builder | RPA incumbent adding agent builder UX. |
| Automation Anywhere | automation:rpa, incumbent | Multi | https://www.automationanywhere.com | RPA incumbent pushing agentic automation. |
| Zapier Agents | automation:ipaas, plg | API | https://zapier.com | iPaaS with agentic steps called “Agents”. |
| Make AI Agents | automation:ipaas, plg | API | https://www.make.com | iPaaS with AI agent features. |
| n8n | automation:workflow, open_source, community | Multi | https://n8n.io | OSS workflow automation; major community + AI workflow expansion. |
| Tray.io Merlin Agent Builder | automation:ipaas, enterprise | API | https://tray.ai/platform/agent-development | Enterprise iPaaS adding agent builder. |
| Workato Agent Studio | automation:ipaas, enterprise | API | https://www.workato.com/agentic/agent-orchestration | iPaaS vendor adding “agentic AI” + builder surfaces. |
| Boomi Agentstudio | automation:ipaas, incumbent | Multi | https://boomi.com/products/agentstudio/ | iPaaS incumbent adding “Agentstudio.” |
| Kissflow | automation:workflow, low_code_platform | Multi | https://kissflow.com/no-code/kissflow-ai-app-builder-create-apps-faster/ | Workflow + low-code platform with AI agent positioning. |
| Automaited | automation:workflow | Multi | https://www.automaited.com/platform/workflow-automation | Workflow automation platform with AI agents. |
| Sola | automation:rpa, ai_native | Desktop | https://www.sola.ai | AI-native desktop automation with agentic behavior. |
| Bardeen | automation:browser, plg | Browser | https://www.bardeen.ai/ | Browser automation playbooks with AI agent builder UX. |
| Relay.app | automation:workflow, ai_native | API | https://www.relay.app | AI-first workflow automation builder with agent steps. |

---

## Segment hypotheses

These hypotheses focus on what differentiates winners in UI-first agent/workflow builders once “a canvas” is no longer a moat.

### Hypothesis 1 — The enterprise winner is **hybrid**: visual UX + APIs + **production controls**

Visual builders win in enterprises when they pair **fast iteration** with **deep customizability** — APIs/SDKs/manifest escape hatches — and **production-grade workflow robustness**: versioning, environments, testing, approvals, audit, safe execution.

- **Companies:** `Flowise` `n8n` `Jinba`
- **Falsifiable test:** A pure drag-and-drop tool — no API surface, no escape hatch, minimal governance — becomes the default in large regulated enterprises.

### Hypothesis 2 — **Distribution** solves the **workflow search problem** and drives consolidation

Because “what to automate” is an open-ended search space, the winners are the platforms with a repeatable **distribution engine** that become the default choice and shrink the search space via **templates + usage-driven discovery**. In practice, this looks like **bottom-up**: OSS/community, templates, developer adoption; plus **top-down**: suite embedding, SI/channel, enterprise sales.

- **Companies:** `n8n` `Flowise` `Langflow` `Zapier Agents`
- **Example:** `n8n` used OSS/community + templates to discover use cases, then translated adoption into enterprise GTM.
- **Falsifiable test:** A builder with weak distribution — or only one vector — repeatedly outgrows competitors that combine bottom-up + top-down with a template/use-case discovery engine.

### Hypothesis 3 — Integrations converge; **reliability + governance + deployment ease** differentiate

Most platforms connect to the same systems, so differentiation shifts to **connector quality**: write access, permissions; **workflow reliability**: retries, idempotency, replay/debugging, monitoring; and **deployment ease**: cloud/on‑prem options, environments, admin controls.

- **Companies:** `SmythOS` `Jinba` `Stack AI` `Regrello` `Salesforce Agentforce` `Boomi Agentstudio` `Tray.io Merlin Agent Builder` `UiPath Agent Builder` `Automation Anywhere`
- **Falsifiable test:** A canvas-first product with shallow connectors and weak ops becomes the default for high-stakes production workflows.

### Hypothesis 4 — **Vertical packs** become the differentiation layer for horizontal builders

As the base connector set commoditizes, horizontal builders defend and grow by shipping **vertical packs**: opinionated workflow templates, domain data models/policies, and KPI-linked checks that reduce setup time and narrow the search space.

- **Companies:** `Regrello` `Kissflow` `Voiceflow` `Bardeen`
- **Falsifiable test:** Horizontal builders keep scaling without shipping reusable domain packs, and customers reliably build everything from scratch.

### Hypothesis 5 — Agentic RPA for computer‑use unlocks the long tail only if **maintenance drops**

Computer‑use expands automation to GUI-heavy and legacy work, but it only scales as software rather than services when **breakage rates** and **operator load** fall fast enough to stay economical.

- **Companies:** `Sola` `UiPath Agent Builder` `Automation Anywhere` `Bardeen`
- **Falsifiable test:** Breaks per 1,000 runs and human intervention rates don’t improve materially over time, and deployments stay partner-heavy.
