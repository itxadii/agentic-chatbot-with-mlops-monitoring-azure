import time
from app import app  # Imports your compiled LangGraph app
from langchain_core.messages import HumanMessage

def run_benchmark(query: str, thread_id: str = "benchmark_1"):
    # ... (rest of your setup) ...
    response = app.invoke({"messages": [HumanMessage(content=query)]}, config)
    end_time = time.time()
    
    latency = end_time - start_time
    last_msg = response['messages'][-1]
    
    # Defensive check for usage_metadata (Task 1: MLOps Monitoring)
    output_tokens = 0
    if hasattr(last_msg, 'usage_metadata') and last_msg.usage_metadata:
        output_tokens = last_msg.usage_metadata.get('output_tokens', 0)
    
    throughput = output_tokens / latency if latency > 0 else 0
    
    print(f"--- MLOps Metrics for: '{query}' ---")
    print(f"Latency: {latency:.2f} seconds")
    print(f"Throughput: {throughput:.2f} tokens/sec")
    print(f"Response: {response['messages'][-1].content[:50]}...")
    print("-" * 40)

if __name__ == "__main__":
    # Task 1.3: Test with multiple prompt variations
    test_queries = [
        "What is 25 * 4?",  # Should hit Calculator Node (DAG test)
        "Tell me a short story about a robot in Nashik.", # Should hit LLM Node
        "What was the first thing I asked you?" # Memory test
    ]
    
    for q in test_queries:
        run_benchmark(q)