# Agentic Chatbot with MLOps Monitoring

A production-ready AI Agent built with **LangGraph** and **Azure GPT-4.1-mini**, featuring stateful memory, Directed Acyclic Graph (DAG) routing, and MLOps performance tracking.

## 🚀 Key Features
- **LLM Orchestration:** Built using LangGraph to manage complex state and conversational memory.
- **DAG Routing:** Implemented a Directed Acyclic Graph to optimize costs by routing math queries to a local calculation node and general queries to the LLM.
- **MLOps Monitoring:** Integrated real-time tracking for **Latency** and **Throughput (Tokens/Sec)**.
- **Cloud-Native Deployment:** Containerized using Docker for scalable deployment across environments.

## 🛠️ Tech Stack
- **Framework:** LangGraph, LangChain
- **Model:** Azure OpenAI (GPT-4.1-mini)
- **Infrastructure:** Docker
- **Monitoring:** Python-based performance metrics

## 📈 MLOps Performance Metrics
| Query Type | Latency | Throughput | Node Route |
| :--- | :--- | :--- | :--- |
| Mathematical | ~0.01s | 0.00 t/s | `calculator_node` |
| General LLM | ~2.73s | ~47.94 t/s | `chatbot_node` |
| Context/Memory| ~0.87s | ~20.69 t/s | `chatbot_node` |

## ⚙️ Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd <repo-folder>