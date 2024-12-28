from decouple import config
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
SECRET_KEY = config('OPENAI_API_KEY')
# print(SECRET_KEY)

# LLMs

# llm = OpenAI(
#     model="gpt-3.5-turbo-instruct",
#     temperature=0,
#     max_retries=2,
#     # api_key="...",
#     # base_url="...",
#     # organization="...",
#     # other params...
# )
# response = llm.invoke("Who is Prime Misnister of India ?")
# print(response)

# Chat Models

## Example 1
# chat = ChatOpenAI(
#     model="gpt-4o",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # api_key="...",
#     # base_url="...",
#     # organization="...",
#     # other params...
# )
# response = chat.invoke("Who is Prime Misnister of India ?")
# # print(response)
# print(response.content)

## Example 2
chat = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # api_key="...",
    # base_url="...",
    # organization="...",
    # other params...
)

messages = [
    SystemMessage(content="You are a standup comedian"),
    HumanMessage(content="Who is Prime Misnister of India ?")
]

response = chat.invoke(messages)
print(response)
# print(response.content)