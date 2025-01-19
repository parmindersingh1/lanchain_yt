from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
# print(SECRET_KEY)

# LLMs
llm = OpenAI(openai_api_key=SECRET_KEY)
response = llm.invoke("Who is Prime Minister of India ?")
print(response)

# Chat Models
# Example 1
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# response = chat.invoke("Who is Prime Minister of India ?")
# print(response)
# # print(response.content)

# Example 2
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# messages = [
#     SystemMessage(content="You are a standup comedian"),
#     HumanMessage(content="Who is Prime Minister of India ?"),
# ]
# response = chat.invoke(messages)
# print(response)
