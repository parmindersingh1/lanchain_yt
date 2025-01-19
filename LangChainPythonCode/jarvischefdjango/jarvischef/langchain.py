from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config


def askJarvisChef(recipe_message):
    SECRET_KEY = config('OPENAI_API_KEY')
    chat = ChatOpenAI(openai_api_key=SECRET_KEY)
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "Your name is Jarvis. You are a master chef so First Introduce yourself as Jarivs The Master Chef. You can write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food related queries. If You don't know the answer then tell I don't know the answer.")
    humanMessagePrompt = HumanMessagePromptTemplate.from_template(
        '{asked_recipe}')

    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt, humanMessagePrompt
    ])

    formattedChatPrompt = chatPrompt.format_messages(
        asked_recipe=recipe_message)
    # print("Formatted Chat Prompt: ", formattedChatPrompt)
    response = chat.invoke(formattedChatPrompt)
    return response.content
