from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=SECRET_KEY)

# # Chat Model - Prompt Template

# # Example 1 - Message Prompt Template as Tuples
chatPrompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful assistant that translates {input_language} to {output_language}."),
    ("human", "{text}"),
])
print("Chat Prompt: ", chatPrompt)
print("Chat Prompt Input Variables: ", chatPrompt.input_variables)
formattedChatPrompt = chatPrompt.format_messages(
    input_language="English",
    output_language="French",
    text="I am learning LangChain JS from GeekyShows YT"
)
print("Formatted Chat Prompt: ", formattedChatPrompt)
# response = chat.invoke(formattedChatPrompt)
# print("Response: ", response)
# print("Response Content: ", response.content)

# # Example 2 - Using Message Classes
# sys_template = "You are a helpful assistant that translates {input_language} to {output_language}."
# human_template = "{text}"

# chatPrompt = ChatPromptTemplate.from_messages([
#     SystemMessagePromptTemplate.from_template(sys_template),
#     HumanMessagePromptTemplate.from_template(human_template)
# ])
# print("Chat Prompt: ", chatPrompt)
# print("Chat Prompt Input Variables: ", chatPrompt.input_variables)

# formattedChatPrompt = chatPrompt.format_messages(
#     input_language="English",
#     output_language="French",
#     text="I am learning LangChain JS from GeekyShows YT"
# )
# print("Formatted Chat Prompt: ", formattedChatPrompt)
# response = chat.invoke(formattedChatPrompt)
# print("Response: ", response)
# print("Response Content: ", response.content)

# # Example 3 - Using PromptTemplate
# systemPrompt = PromptTemplate(
#     input_variables=["input_language", "output_language"],
#     template="You are a helpful assistant that translates {input_language} to {output_language}."
# )
# systemPrompt = PromptTemplate.from_template(
#     "You are a helpful assistant that translates {input_language} to {output_language}.")
# humanPrompt = PromptTemplate.from_template("{text}")

# systemMessagePrompt = SystemMessagePromptTemplate(prompt=systemPrompt)
# humanMessagePrompt = HumanMessagePromptTemplate(prompt=humanPrompt)

# chatPrompt = ChatPromptTemplate.from_messages([
#     systemMessagePrompt, humanMessagePrompt
# ])
# print("Chat Prompt: ", chatPrompt)
# print("Chat Prompt Input Variable : ", chatPrompt.input_variables)

# formattedChatPrompt = chatPrompt.format_messages(
#     input_language="English",
#     output_language="French",
#     text="I love programming"
# )
# print("Formatted Chat Prompt: ", formattedChatPrompt)
# response = chat.invoke(formattedChatPrompt)
# print("Response: ", response)
# print("Response Content: ", response.content)
