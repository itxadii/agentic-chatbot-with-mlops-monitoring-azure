from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from agent.state import AgentState
from agent.nodes import chatbot_node, calculator_node

def route_question(state: AgentState):
    """Routing logic (DAG) to decide the next node."""
    user_input = state["messages"][-1].content.lower()
    if any(op in user_input for op in ["+", "-", "*", "/", "calculate"]):
        return "calculator"
    return "chatbot"

# Build the Graph
workflow = StateGraph(AgentState)

workflow.add_node("chatbot", chatbot_node)
workflow.add_node("calculator", calculator_node)

# DAG Routing
workflow.add_conditional_edges(START, route_question)
workflow.add_edge("chatbot", END)
workflow.add_edge("calculator", END)

# Compile with Memory for persistence
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)