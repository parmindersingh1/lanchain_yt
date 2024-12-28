from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

chat = ChatOllama(model="llama3.2:latest")

# Chat Model
# Few Shot Examples
examples = [
    {
        "input": "2+2",
        "output": "4"
    },
    {
        "input": "2+3",
        "output": "5"
    }
]

example_prompt = ChatPromptTemplate.from_messages([
    ('human', "{input}"),
    ('ai', "{output}")
])

# print("Example Prompt", example_prompt)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)
# print("Few Shot Prompt", few_shot_prompt.format())

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful math problem solver."),
    few_shot_prompt,
    ("human", "{input}")
])

# print("Final Prompt", final_prompt)

formattedChatPrompt = final_prompt.format_messages(
    input="what is the square of a triangle?"
)

# print("Formatted Chat Prompt", formattedChatPrompt)

response = chat.invoke(formattedChatPrompt)

print("Response content: ", response.content)