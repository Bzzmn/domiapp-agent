"""This file was generated using `langgraph-gen` version 0.0.3.

This file provides a placeholder implementation for the corresponding stub.

Replace the placeholder implementation with your own logic.
"""

from typing_extensions import TypedDict
from state import UserState
from stub import CustomAgent
from nodes import should_end
from langchain_openai import ChatOpenAI
from tools.tools_registry import agent_tools
from langgraph.prebuilt import ToolNode

llm = ChatOpenAI(model="gpt-4o-mini")
llm = llm.bind_tools(agent_tools)
llm = llm.bind(tool_choice="auto")

tools_node = ToolNode(tools=agent_tools)

class SomeState(TypedDict):
    # define your attributes here
    foo: str


# Define stand-alone functions
def agent(state) -> dict:
    print("In node: agent")
    base_prompt = """
    Eres Domi, un asistente de IA que puede responder preguntas y realizar tareas relacionadas con los procesos de revision de documentos para permisos de edificación, revisar la normativa y proporcionar información relevante.
    Comienza con un saludo y una introducción.
    Cuentas con una herramienta para obtener la fecha y hora actual.
    """
    messages = [
        ("system", base_prompt),
        ("user", state["messages"][-1].content)
    ]

    response = llm.invoke(messages)
    return {
        "messages": [response]
    }

def tools(state) -> dict:
    print("In node: tools")
    return {
        # Add your state update logic here
    }



agent = CustomAgent(
    state_schema=UserState,
    impl=[
        ("agent", agent),
        ("tools", tools),
        ("conditional_edge_1", should_end),
    ],
)

app = agent.compile()
