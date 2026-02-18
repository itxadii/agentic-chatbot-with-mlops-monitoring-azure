import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage
from agent.state import AgentState

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
    """Handles math-related queries locally to save costs."""
    # In a real app, you'd parse the numbers here.
    result = "Calculator Node: I detected a math query and processed the result locally."
    return {
        "messages": [
            AIMessage(
                content=result,
                usage_metadata={"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
            )
        ]
    }