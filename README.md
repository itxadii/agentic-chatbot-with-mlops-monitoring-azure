# Agentic Chatbot with MLOps Monitoring

A production-ready AI agent built with LangGraph and Azure GPT-4.1-mini, featuring stateful memory, Directed Acyclic Graph (DAG) routing, and real-time MLOps performance tracking.

---

## Overview

This project demonstrates a fully orchestrated conversational AI system designed for production environments. It combines intelligent query routing via a DAG architecture with continuous performance monitoring, enabling cost-efficient LLM usage without sacrificing response quality.

---

## Key Features

- **LLM Orchestration:** Built with LangGraph to manage complex state transitions and persistent conversational memory across multi-turn interactions.
- **DAG Routing:** A Directed Acyclic Graph routes mathematical queries to a lightweight local calculation node and general queries to the LLM, reducing unnecessary token consumption.
- **MLOps Monitoring:** Real-time tracking of latency and throughput (tokens per second) for every query type and routing path.
- **Prompt Engineering:** System prompt variants were benchmarked; the selected "Concise Professional" variant reduced output tokens by 15% while maintaining accuracy, lowering overall latency.
- **Cloud-Native Deployment:** Fully containerized with Docker for consistent, scalable deployment across environments.

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| Orchestration Framework | LangGraph, LangChain |
| Language Model | Azure OpenAI (GPT-4.1-mini) |
| Infrastructure | Docker |
| Monitoring | Python-based performance metrics |

---

## MLOps Performance Metrics

| Query Type | Latency | Throughput | Routed Node |
| :--- | :--- | :--- | :--- |
| Mathematical | ~0.01s | 0.00 t/s | `calculator_node` |
| General LLM | ~2.73s | ~47.94 t/s | `chatbot_node` |
| Context / Memory | ~0.87s | ~20.69 t/s | `chatbot_node` |

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/itxadii/agentic-chatbot-with-mlops-monitoring-azure.git
cd agentic-chatbot-with-mlops-monitoring-azure
```

### 2. Configure Environment Variables

Create a `.env` file in the project root based on the provided template:

```bash
cp .env.example .env
```

Open `.env` and fill in your Azure OpenAI credentials:

```
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
AZURE_OPENAI_API_VERSION=your_api_version
```

### 3. Build and Run with Docker

```bash
docker build -t ai-agent-monitor .
docker run ai-agent-monitor
```

---

## Project Structure

```
.
├── agent/
│   ├── graph.py          # LangGraph DAG definition and node routing
│   ├── nodes.py          # chatbot_node and calculator_node implementations
│   └── state.py          # Shared state schema
├── monitoring/
│   └── metrics.py        # Latency and throughput tracking
├── .env.example          # Environment variable template
├── Dockerfile
└── main.py               # Entry point
```

---

## How It Works

1. A user query enters the graph via the entry node.
2. The router inspects the query and directs it to either `calculator_node` (for math expressions) or `chatbot_node` (for general and context-dependent queries).
3. The response is generated and performance metrics (latency, tokens per second) are logged in real time.
4. Conversational memory is persisted in the graph state, enabling coherent multi-turn dialogue.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.