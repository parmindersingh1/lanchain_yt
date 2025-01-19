from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from decouple import config
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
SECRET_KEY = config('OPENAI_API_KEY')
# Basic Streaming 1
chat = ChatOpenAI(openai_api_key=SECRET_KEY, streaming=True,
                  callbacks=[StreamingStdOutCallbackHandler()])
chat_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        "Tell me a long story about {topic}")
])
formatted_chat_prompt = chat_prompt.format_messages(topic="king arthur")
response = chat.invoke(formatted_chat_prompt)
print(response.content)

# # Basic Streaming 2
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# chat_prompt = ChatPromptTemplate.from_messages([
#     HumanMessagePromptTemplate.from_template(
#         "Tell me a fact about {topic}")
# ])
# formatted_chat_prompt = chat_prompt.format_messages(topic="king arthur")
# response = chat.stream(formatted_chat_prompt)
# for res in response:
#     print(res.content, end="", flush=True)

# # Streaming in Chain
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# chat_prompt = ChatPromptTemplate.from_template("Tell me a fact about {topic}")
# chain = chat_prompt | chat | StrOutputParser()
# response = chain.stream({"topic": "Python"})
# for res in response:
#     print(res, end="", flush=True)

# # Streaming with Agents
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# # Create Agent
# prompt = hub.pull("hwchase17/openai-functions-agent")

# search = DuckDuckGoSearchRun()

# tools = [search]
# agent = create_openai_functions_agent(llm=chat, tools=tools, prompt=prompt)
# # Run Agent
# agent_executor = AgentExecutor(agent=agent, tools=tools)
# response = agent_executor.stream(
#     {"input": "Who is current Prime Minister of India?"})
# for res in response:
#     # Agent Action
#     if "actions" in res:
#         for action in res["actions"]:
#             print(
#                 f"Calling Tool: `{action.tool}` with input `{action.tool_input}`")
#     # Observation
#     elif "steps" in res:
#         for step in res["steps"]:
#             print(f"Tool Result: `{step.observation}`")
#     # Final result
#     elif "output" in res:
#         print(f'Final Output: {res["output"]}')
#     else:
#         raise ValueError()
#     print("---")
