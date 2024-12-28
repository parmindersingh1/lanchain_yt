from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from decouple import config


def askJarvsChef(recipe_message):
    SECRET_KEY = config('OPENAI_API_KEY')
    # chat = ChatOpenAI(openai_api_key=SECRET_KEY)
    chat = ChatOllama(model="llama3.2:latest")
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        """your name is Jarvis. You are a master chef so First Introduce yourself as Jarvis The Master Chef. You can write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food related queries. If ypu don't know the answer then tell I don't know the answer.
        If you don't know don't provide sample recipe"""
    )

    humanMessagePrompt = HumanMessagePromptTemplate.from_template("{asked_recipe}")

    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt,   humanMessagePrompt
    ])

    formattedChatPrompt = chatPrompt.format_messages(asked_recipe=recipe_message)
    # print("Formatted Prompt", formattedChatPrompt)
    response = chat.invoke(formattedChatPrompt)
    return response.content
