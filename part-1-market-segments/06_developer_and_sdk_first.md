---
title: "Company Type 1: Developer & SDK-first"
status: "Active research — v3"
---

# Company type 1: Developer & SDK-first platforms, frameworks, and infrastructure

## Segment definition

- They serve developer teams building agentic products for production environments.
- They serve platform teams that need predictable primitives, not opaque “magic.”

## What they build

- They build agent runtimes and managed services: “Agent OS” platforms.
- They build framework SDKs for orchestration, state, memory, and tool use.
- They build computer‑use environments: browser/desktop sessions plus reliability tooling.

## Scope

This page is intentionally scoped to three developer-first sub‑segments:

1) **Foundation + cloud “Agent OS” providers** — agent runtimes / managed services shipped by model providers, clouds, and major platforms  
2) **Agent framework SDKs** — pro‑code frameworks for building/orchestrating agents  
3) **Computer‑use / browser & desktop SDKs** — environment tooling that lets agents act on UIs

**Validated companies:** 39 — only included after checking the primary link

---

## A) Foundation + cloud "Agent OS" providers

| Company | Tags | Primary link |
|---|---|---|
| OpenAI | foundation, agent runtime, AgentKit/Responses/Agents | https://platform.openai.com/docs/guides/agents |
| Anthropic | foundation, agent SDK, MCP ecosystem | https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk |
| Google Cloud Vertex AI | cloud, managed agent builder, ADK/Agent Engine | https://cloud.google.com/products/agent-builder |
| AWS Amazon Bedrock AgentCore | cloud, managed agent runtime | https://aws.amazon.com/bedrock/agentcore/ |
| IBM watsonx Orchestrate | enterprise, agent builder | https://www.ibm.com/products/watsonx-orchestrate/ai-agent-builder |
| Databricks Agent Bricks | data platform, managed agent systems | https://docs.databricks.com/aws/en/generative-ai/agent-bricks/ |
| Microsoft Semantic Kernel | framework, open-source | https://github.com/microsoft/semantic-kernel |
| Microsoft AutoGen | multi-agent framework, open-source | https://github.com/microsoft/autogen |
| Snowflake Cortex Agents | data platform, agentic workflow API | https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents |
| Mistral Agents API | foundation, agents API | https://docs.mistral.ai/agents/introduction |
| Cohere — tool use & agents | foundation, tool use, agentic apps | https://docs.cohere.com/docs/building-an-agent-with-cohere |

---

## B) Agent framework SDKs

| Company | Tags | Primary link |
|---|---|---|
| OpenAI Agents SDK | sdk, lightweight primitives | https://openai.github.io/openai-agents-python/ |
| LangChain | framework, open-source | https://github.com/langchain-ai/langchain |
| LangGraph | orchestration, stateful agents, deployment | https://github.com/langchain-ai/langgraph |
| Mozilla.ai Agent Platform | agent platform, enterprise automation | https://www.mozilla.ai/product/agent-platform |
| CrewAI | multi-agent framework | https://github.com/crewAIInc/crewAI |
| LlamaIndex | framework, retrieval + agents | https://github.com/run-llama/llama_index |
| Haystack | framework, pipelines + agents | https://github.com/deepset-ai/haystack |
| Mastra | framework, deployable agents | https://github.com/mastra-ai/mastra |
| PydanticAI | framework, typed agents | https://github.com/pydantic/pydantic-ai |
| Hugging Face smolagents | framework, open-source | https://github.com/huggingface/smolagents |
| DSPy | framework, optimization/compilation | https://github.com/stanfordnlp/dspy |
| Letta | stateful agents, memory | https://www.letta.com/ |
| Agno | multi-agent framework + runtime | https://github.com/agno-agi/agno |
| BeeAI Framework | framework, multi-agent systems | https://github.com/i-am-bee/beeai-framework |
| Cerebrum — AIOS SDK | open-source, agent OS research | https://github.com/agiresearch/AIOS |
| AutoAgent | open-source, agent framework | https://github.com/HKUDS/AutoAgent |

---

## C) Computer-use / browser & desktop SDKs

| Company | Tags | Primary link |
|---|---|---|
| Browserbase Stagehand | browser SDK, OSS + cloud browser infra | https://docs.stagehand.dev/ |
| Cyberdesk | desktop environment API, SDKs | https://docs.cyberdesk.io/ |
| TinyFish / AgentQL | web automation, query language + SDKs | https://docs.agentql.com/home |
| Skyvern | browser automation, open-source | https://github.com/Skyvern-AI/skyvern |
| Steel.dev | browser infrastructure for agents | https://steel.dev/ |
| Anchor Browser | browser sessions + SDK | https://docs.anchorbrowser.io/introduction |
| Induced AI | browser sessions API, autonomous tasks | https://docs.induced.ai/introduction |
| Scrapybara | cloud browsers / virtual desktops for agents | https://scrapybara.com/ |
| Browser Use | open-source browser agent library | https://github.com/browser-use/browser-use |
| Magnitude | vision-first browser agent framework | https://docs.magnitude.run/getting-started/introduction |
| MultiOn | web action API | https://docs.multion.ai/welcome |
| Simular AI — Agent S | computer-use agent framework | https://github.com/simular-ai/Agent-S |
| Anon.com | browser automation, secure web integrations | https://www.anon.com/ |

---

## Segment hypotheses

### Hypothesis 1 — **Production trust** compounds: layered primitives with an **ops path** win

Developer-first winners pair **predictable primitives** with a **production ops path**: deployment, traces, eval gates, and feedback loops. Once teams hit **real traffic + on‑call**, “framework-only” stacks get swapped out.

- **Companies:** `LangChain` `Mastra` `Letta` `OpenAI Agents SDK`
- **Falsifiable test:** What % of teams keep the same framework after their first production incidents?

### Hypothesis 2 — **Computer‑use environment control** is a durable wedge

For agents acting in messy browsers/desktops, the moat is **execution environment control**: sessions, replays, long‑lived auth, retries, and audit. This turns “agent reliability” into **infrastructure**.

- **Companies:** `Browserbase Stagehand` `Cyberdesk` `Browser Use`
- **Falsifiable test:** In production, specialized “computer‑use infra” does *not* reduce incident rate, MTTR, or operator load vs generic stacks.

### Hypothesis 3 — **Context optimization** compounds; value capture depends on **feedback artifacts**

The compounding advantage is owning the **context layer**: memory, retrieval, prompt/program optimization, plus the **feedback loop**: logs → evals/grades → updates. Durable leverage depends on who owns **telemetry, labels, and tuned artifacts**.

- **Companies:** `OpenAI` `Agno` `Letta` `DSPy`
- **Note:** `Letta` and `DSPy` are focused on **context optimization**.
- **Falsifiable test:** Customers routinely demand portability of tuned artifacts + telemetry, and closed-loop ownership stops correlating with durability.
