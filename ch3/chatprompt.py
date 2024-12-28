from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

chat = ChatOllama(model="llama3.2:latest")

# Chat Model - Prompt Template

# Example 1 - Message Prompt Template as Tuples
# chatPrompt = ChatPromptTemplate.from_messages([
#     ('system', "you are a helpful assistant that translates {input_language} to {output_language}."), #told the system how to behave
#     ('human', "{text}"),
# ])

# # print("Chat Prompt: ", chatPrompt)
# # print("Chat Prompt Input variables: ", chatPrompt.input_variables)
# formattedChatPrompt = chatPrompt.format_messages(input_language = "English", output_language = "Hindi", text = "I am Learning Lagchain from GeekyShows YT")

# # print("Formatted Chat Prompt: ", formattedChatPrompt)

# response = chat.invoke(formattedChatPrompt)
# print("Response: ", response.content)

# Example 2 - Using Message Classes
# sys_template = "you are a helpful assistant that translates {input_language} to {output_language}."
# human_template = "{text}"

# chatPrompt = ChatPromptTemplate.from_messages([
#    SystemMessagePromptTemplate.from_template(sys_template),
#    HumanMessagePromptTemplate.from_template(human_template)
# ])

# # print("Chat Prompt: ", chatPrompt)
# # print("Chat Prompt Input variables: ", chatPrompt.input_variables)
# formattedChatPrompt = chatPrompt.format_messages(input_language = "English", output_language = "Hindi", text = "I am Learning Lagchain from GeekyShows YT")

# # print("Formatted Chat Prompt: ", formattedChatPrompt)

# response = chat.invoke(formattedChatPrompt)
# print("Response: ", response.content)

#  Example 3 - Using PrmptTemplate
systemPrompt = PromptTemplate(
    input_variables=["input_language", "output_language"],
    template= "you are a helpful assistant that translates {input_language} to {output_language}."
)
# systemPrompt = PromptTemplate.from_template("you are a helpful assistant that translates {input_language} to {output_language}.")
humanPrompt = PromptTemplate.from_template("{text}")

# print("System Prompt: ", systemPrompt)

systemMessagePrompt = SystemMessagePromptTemplate(prompt=systemPrompt)
humanMessagePrompt = HumanMessagePromptTemplate(prompt=humanPrompt)

chatPrompt = ChatPromptTemplate.from_messages([
    systemMessagePrompt,   humanMessagePrompt
])

# # print("Chat Prompt: ", chatPrompt)
# # print("Chat Prompt Input variables: ", chatPrompt.input_variables)

formattedChatPrompt = chatPrompt.format_messages(input_language = "English", output_language = "Hindi", text = "I love programming")

# print("Formatted Chat Prompt: ", formattedChatPrompt)

response = chat.invoke(formattedChatPrompt)
print("Response: ", response.content)