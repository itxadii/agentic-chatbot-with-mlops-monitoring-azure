# Agentic Chatbot with LangGraph Routing and Runtime Monitoring

A modular, containerized conversational AI system built using LangGraph and Azure OpenAI. The project demonstrates explicit DAG-based routing, stateful conversation handling, and lightweight runtime performance monitoring.

---

## Overview

This project showcases how LangGraph can be used to orchestrate an AI agent workflow using a Directed Acyclic Graph (DAG). The system routes simple, deterministic queries (such as mathematical expressions) to local logic, while delegating general and contextual queries to a Large Language Model (LLM).

The primary goal is to demonstrate controlled LLM usage, explicit execution flow, and basic observability, rather than a fully hardened production system.

---

## Key Features

### LangGraph-based Orchestration
- Explicit DAG definition using LangGraph
- Clear separation between state, nodes, and routing logic
- Predictable execution flow with guaranteed termination

### Deterministic Query Routing
- Simple rule-based routing logic directs mathematical queries to a local calculator node
- General and context-dependent queries are handled by the LLM
- Reduces unnecessary LLM calls for trivial operations

### Stateful Conversation Handling
- Conversation history is maintained in shared graph state during execution
- Enables coherent multi-turn interactions within a single process lifecycle

### Runtime Performance Monitoring
- Latency and throughput (tokens per second) are measured per execution path
- Useful for comparing performance between local computation and LLM responses

### Containerized Execution
- Fully containerized using Docker
- Reproducible execution across environments

---

## Tech Stack

| Layer | Technology |
|---|---|
| Orchestration | LangGraph, LangChain |
| Language Model | Azure OpenAI (GPT-4.1-mini) |
| Runtime | Python |
| Containerization | Docker |
| Monitoring | Custom Python metrics |

---

## Example Runtime Observations

| Query Type | Routed Node | Notes |
|---|---|---|
| Mathematical | `calculator_node` | Near-instant execution using local logic |
| General Query | `chatbot_node` | LLM-based response with higher latency |
| Contextual Query | `chatbot_node` | Uses conversation history from graph state |

> Metrics are indicative and depend on runtime environment and model configuration.

---

## Project Structure

```
.
├── agent/
│   ├── graph.py          # LangGraph DAG and routing logic
│   ├── nodes.py          # Calculator and chatbot node implementations
│   └── state.py          # Shared graph state definition
├── monitoring/
│   └── metrics.py        # Runtime latency and throughput tracking
├── .env.example
├── Dockerfile
└── main.py               # Application entry point
```

---

## How It Works

1. User input enters the graph at the `START` node.
2. A routing function inspects the input and selects the next node.
3. The selected node processes the request and updates the shared state.
4. Runtime metrics are recorded.
5. The graph execution terminates at `END`.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/itxadii/agentic-chatbot-with-mlops-monitoring-azure.git
cd agentic-chatbot-with-mlops-monitoring-azure
```

### 2. Configure Environment Variables

```bash
cp .env.example .env
```

Fill in Azure OpenAI credentials in `.env`.

### 3. Build and Run

```bash
docker build -t ai-agent-monitor .
docker run ai-agent-monitor
```

---

## Prompt Engineering Insights

Tested three variations of system prompts to balance detail and speed. The final implementation uses a "Concise Assistant" prompt, which optimized throughput by ~15% compared to the default "Helpful Assistant" prompt, without losing accuracy for Nashik-specific contextual queries.

---

## Notes and Limitations

- State is persisted in memory only and does not survive process restarts.
- The project focuses on orchestration and runtime behavior, not full MLOps pipelines.
- Intended as a learning and demonstration project for LangGraph-based agent workflows.

---

## License

MIT License.