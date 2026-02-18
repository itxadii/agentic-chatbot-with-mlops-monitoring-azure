import os
from dotenv import load_dotenv
load_dotenv()

from agent.graph import app
from monitoring.metrics import run_benchmark

if __name__ == "__main__":
    queries = [
        "What is 50 + 50?",
        "Tell me a story about Nashik engineering.",
        "What was the first thing I asked you?"
    ]
    
    print("--- Starting MLOps Benchmark ---")
    for i, q in enumerate(queries):
        metrics = run_benchmark(app, q, thread_id="session_1")
        print(f"Test {i+1}: {metrics}")