from typing import Optional, Literal
from typing_extensions import TypedDict
from langgraph.graph import add_messages
from langchain_core.messages import AnyMessage
from typing_extensions import Annotated
from datetime import datetime




class UserState(TypedDict, total=False):
    messages: Annotated[list[AnyMessage], add_messages]