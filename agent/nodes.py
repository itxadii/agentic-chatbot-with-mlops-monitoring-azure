import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage
from agent.state import AgentState
import re

# Initialize the LLM once
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0
)

def chatbot_node(state: AgentState):
    """Processes general queries using Azure GPT-4.1-mini."""
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def calculator_node(state: AgentState):
    """Actually calculates values from the user input."""
    user_msg = state["messages"][-1].content
    
    # Simple regex to find numbers and an operator
    match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', user_msg)
    
    if match:
        num1, op, num2 = match.groups()
        num1, num2 = int(num1), int(num2)
        
        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/': result = num1 / num2 if num2 != 0 else "Error: Div by zero"
        
        content = f"Calculator Node: The result of {num1} {op} {num2} is {result}."
    else:
        content = "Calculator Node: I couldn't parse the math expression, but the route worked!"

    return {
        "messages": [
            AIMessage(
                content=content,
                usage_metadata={"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
            )
        ]
    }