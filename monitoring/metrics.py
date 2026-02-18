import time
from langchain_core.messages import HumanMessage

def run_benchmark(app, query: str, thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    
    start_time = time.time()
    response = app.invoke({"messages": [HumanMessage(content=query)]}, config)
    latency = time.time() - start_time
    
    last_msg = response['messages'][-1]
    output_tokens = 0
    if hasattr(last_msg, 'usage_metadata') and last_msg.usage_metadata:
        output_tokens = last_msg.usage_metadata.get('output_tokens', 0)
    
    throughput = output_tokens / latency if latency > 0 else 0
    
    return {
        "query": query,
        "latency": f"{latency:.2f}s",
        "throughput": f"{throughput:.2f} t/s",
        "response": last_msg.content[:50]
    }