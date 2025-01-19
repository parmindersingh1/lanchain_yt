from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_openai_functions_agent, AgentExecutor, create_react_agent
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain import hub
from langchain_openai import ChatOpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# Agent Type - OpenAI Functions
# Create Agent
prompt = hub.pull("hwchase17/openai-functions-agent")
# print(prompt)
search = DuckDuckGoSearchRun()

tools = [search]
agent = create_openai_functions_agent(llm=chat, tools=tools, prompt=prompt)
# Run Agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

response = agent_executor.invoke(
    {"input": "Who is current Prime Minister of India?"})
print(response)

# # # Agent Type - ReAct
# # Create Agent
# prompt = hub.pull("hwchase17/react")
# # print(prompt)
# search = DuckDuckGoSearchRun()

# tools = [search]
# agent = create_react_agent(llm=chat, tools=tools, prompt=prompt)
# # Run Agent
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = agent_executor.invoke(
#     {"input": "Who is current Prime Minister of India?"})
# print(response)

# Custom Tool
# # Using Decorator
# class SearchInput(BaseModel):
#     query: str = Field(description="should be a search query")


# @tool("search-tool", args_schema=SearchInput, return_direct=True)
# def search(query: str) -> str:
#     """Look up things online"""
#     return "Langchain"

# print(search.name)
# print(search.description)
# print(search.args)

# # Using StructuredTool
# class CalculatorInput(BaseModel):
#     a: int = Field(description="first number")
#     b: int = Field(description="second number")


# def multiply(a: int, b: int) -> int:
#     "Multiply two numbers"
#     return a * b


# calculator = StructuredTool.from_function(
#     func=multiply,
#     name="Calculator",
#     description="multiply numbers",
#     args_schema=CalculatorInput,
#     return_direct=True,
# )
# print(calculator.name)
# print(calculator.description)
# print(calculator.args)

# # Using Custom Tool
# # Defining Custom Tool
# @tool
# def get_word_length(words: str) -> int:
#     """Returns the length of a word"""
#     return len(words)


# # Create Agent
# prompt = hub.pull("hwchase17/react")

# tools = [get_word_length]
# agent = create_react_agent(llm=chat, tools=tools, prompt=prompt)
# # Run Agent
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = agent_executor.invoke(
#     {"input": "Hello"})
# print(response)

# # Multiple Tools
# # Defining Custom Tool
# @tool
# def get_word_length(word: str) -> int:
#     """Returns the length of a word."""
#     return len(word)


# # Create Agent
# prompt = hub.pull("hwchase17/react")
# search = DuckDuckGoSearchRun()
# tools = [get_word_length, search]
# agent = create_react_agent(llm=chat, tools=tools, prompt=prompt)
# # Run Agent
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# response = agent_executor.invoke(
#     {"input": "What is LangChain ? What is the total word length of that including space ?"})
