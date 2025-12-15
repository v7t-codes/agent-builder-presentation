---
title: "Company Type 1: Developer & SDK-first"
status: "Active research (v3)"
---

# Company type 1: Developer & SDK-first platforms, frameworks, and infrastructure

## Segment definition (who they serve)

- Developer teams building agentic products in production
- Platform teams that need predictable primitives (not “magic”)

## What they build

- Agent runtimes and managed services (“Agent OS” platforms)
- Framework SDKs for orchestration, state, memory, and tool use
- Computer‑use environments (browser/desktop sessions + reliability tooling)

## Scope (this page)

This page is intentionally scoped to three developer-first sub‑segments:

1) **Foundation + cloud “Agent OS” providers** (agent runtimes / managed services shipped by model providers, clouds, and major platforms)  
2) **Agent framework SDKs** (pro‑code frameworks for building/orchestrating agents)  
3) **Computer‑use / browser & desktop SDKs** (environment tooling that lets agents act on UIs)

**Validated companies:** 39 (only included after checking the primary link)

---

## A) Foundation + cloud “Agent OS” providers

| Company | Tags | Primary link |
|---|---|---|
| OpenAI | foundation, agent runtime, AgentKit/Responses/Agents | https://platform.openai.com/docs/guides/agents |
| Anthropic | foundation, agent SDK, MCP ecosystem | https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk |
| Google Cloud Vertex AI | cloud, managed agent builder, ADK/Agent Engine | https://cloud.google.com/products/agent-builder |
| AWS Amazon Bedrock AgentCore | cloud, managed agent runtime | https://aws.amazon.com/bedrock/agentcore/ |
| IBM watsonx Orchestrate | enterprise, agent builder | https://www.ibm.com/products/watsonx-orchestrate/ai-agent-builder |
| Databricks Agent Bricks | data platform, managed agent systems | https://docs.databricks.com/aws/en/generative-ai/agent-bricks/ |
| Mozilla.ai Agent Platform | agent platform, enterprise automation | https://www.mozilla.ai/product/agent-platform |
| Snowflake Cortex Agents | data platform, agentic workflow API | https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents |
| Mistral Agents API | foundation, agents API | https://docs.mistral.ai/agents/introduction |
| Cohere (Tool use & agents) | foundation, tool use, agentic apps | https://docs.cohere.com/docs/building-an-agent-with-cohere |

---

## B) Agent framework SDKs

| Company | Tags | Primary link |
|---|---|---|
| OpenAI Agents SDK | sdk, lightweight primitives | https://openai.github.io/openai-agents-python/ |
| LangChain | framework, open-source | https://github.com/langchain-ai/langchain |
| LangGraph | orchestration, stateful agents, deployment | https://github.com/langchain-ai/langgraph |
| Microsoft Semantic Kernel | framework, open-source | https://github.com/microsoft/semantic-kernel |
| Microsoft AutoGen | multi-agent framework, open-source | https://github.com/microsoft/autogen |
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
| Cerebrum (AIOS SDK) | open-source, agent OS research | https://github.com/agiresearch/AIOS |
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
| Simular AI (Agent S) | computer-use agent framework | https://github.com/simular-ai/Agent-S |

---

## Segment hypotheses (investable theses)

### Hypothesis 1 — Production trust compounds: layered primitives with an ops path win

**Claim:** In dev-first agent building, the durable winners combine two things:

1) **Developer trust** (predictable primitives, visible failure modes, minimal “magic”), and  
2) **A real path to production** (deployment shape, traces/logs, eval gates, and operational feedback loops).

Frameworks that are either (a) “local-only orchestration” or (b) “opaque abstraction” get swapped out once teams hit real traffic and on‑call reality.

**Companies that fit the pattern (examples):**

- **OpenAI Agents SDK** — explicitly “lightweight” primitives for agent building: https://github.com/openai/openai-agents-python
- **LangGraph** — low-level, stateful orchestration with durable execution + deployment tooling via LangSmith: https://github.com/langchain-ai/langgraph
- **Mastra** — explicit “prototype → production” framing with built-in evals + observability: https://github.com/mastra-ai/mastra
- **Letta** — stateful agents with persistent memory (database-backed state): https://docs.letta.com/stateful-agents/
- **Cloud “Agent OS” platforms** (pressure + distribution) — production deployment/ops bundled at the platform layer: https://cloud.google.com/products/agent-builder ; https://aws.amazon.com/bedrock/agentcore/

**Counter-pressure:** If platform-native agent operations become standardized and effortless, independent frameworks must win on workflow fit, portability, and trust — or they become thin wrappers.

**Falsifiable test:** Track production retention: what % of teams keep the same framework after (a) real traffic and (b) their first on‑call incidents.

**Weight now:** High

### Hypothesis 2 — Computer‑use environment control is a durable wedge

**Claim:** For agents acting in messy browsers/desktops, value concentrates in owning the execution environment: sessions, replays, logs, retries, long‑lived authenticated runs, and audit-friendly behavior. This turns “agent reliability” from a model problem into an infrastructure problem.

**Evidence (examples):**

- Browserbase Stagehand focuses on reliable browser automation (natural language + code): https://docs.stagehand.dev/
- Cyberdesk is explicit about virtual desktops for agents (SDK-triggered runs; legacy workflows): https://docs.cyberdesk.io/

**Companies to watch (examples):** Browserbase Stagehand, Cyberdesk, Steel.dev, Scrapybara, Anchor Browser, Induced AI, Skyvern (primary links in the tables above).

**Counter-pressure:** Model providers may commoditize parts of computer‑use (vision, navigation, tool calling). The moat shifts to reliability under audit and failure-mode management.

**Falsifiable test:** In production deployments, compare incident rate, MTTR, and operator load between generic automation stacks and specialized “computer‑use infra.”

**Weight now:** High

### Hypothesis 3 — Closed-loop optimization compounds; value capture depends on who owns feedback artifacts

**Claim:** The compounding advantage is not “we have an agent,” it’s “we have a feedback loop that improves it” (evaluation, grading, and training workflows). Durable value depends on who owns the logs, labels, and tuned artifacts.

**Evidence (examples):**

- OpenAI Cookbook: reinforcement fine-tuning workflows for grader‑driven improvement: https://github.com/openai/openai-cookbook/blob/main/examples/Reinforcement_Fine_Tuning.ipynb
- OpenAI Cookbook: improving tool reliability via fine‑tuning for function calling: https://github.com/openai/openai-cookbook/blob/main/examples/Fine_tuning_for_function_calling.ipynb
- Mastra positions “built-in evals + observability” as the ongoing refinement loop: https://github.com/mastra-ai/mastra

**Companies to watch (examples):** OpenAI, Mastra, LangGraph/LangSmith, Databricks (Agent Bricks), Snowflake (Cortex Agents), and cloud platforms that own the logging and deployment surface (primary links above).

**Counter-pressure:** If customers demand full portability of tuned artifacts and logs, “closed loop” becomes a features race rather than a moat.

**Falsifiable test:** Track procurement terms over time: do customers increasingly require portability of tuned artifacts and operational telemetry?

**Weight now:** High as a technical dynamic; medium as a durable moat
