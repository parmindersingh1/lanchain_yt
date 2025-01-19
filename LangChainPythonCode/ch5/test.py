from langchain.output_parsers import DatetimeOutputParser, CommaSeparatedListOutputParser, PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=SECRET_KEY)

# # Example 1
date_time_parser = DatetimeOutputParser()
print(date_time_parser.get_format_instructions())

comma_sep_parser = CommaSeparatedListOutputParser()
print(comma_sep_parser.get_format_instructions())

# Example 2
# date_time_parser = DatetimeOutputParser()
# human_template = "{request}\n{format_instruction}"
# chat_prompt = ChatPromptTemplate.from_messages([
#     HumanMessagePromptTemplate.from_template(human_template)
# ])

# # print("Chat Prompt: ", chat_prompt)
# formatted_chat_prompt = chat_prompt.format_messages(
#     request="What date was when world war 2 declared",
#     format_instruction=date_time_parser.get_format_instructions()
# )
# # print("Formatted Chat Prompt: ", formatted_chat_prompt)
# # response = chat.invoke(formatted_chat_prompt)
# # print("Response Content: ", response.content)
# # print("Response Content Parse: ", date_time_parser.parse(response.content))

# # Example 3
# # Define your desired data structure.


# class Cricketer(BaseModel):
#     name: str = Field(description="Name of Cricketer")
#     records: list = Field(description="Python list of records")


# parser = PydanticOutputParser(pydantic_object=Cricketer)
# # print(parser.get_format_instructions())
# human_template = "{request}\n{format_instruction}"
# chat_prompt = ChatPromptTemplate.from_messages([
#     HumanMessagePromptTemplate.from_template(human_template)
# ])

# formatted_chat_prompt = chat_prompt.format_messages(
#     request="tell me about a cricketer",
#     format_instruction=parser.get_format_instructions()
# )

# # print("Formatted Chat Prompt: ", formatted_chat_prompt)
# # response = chat.invoke(formatted_chat_prompt)
# # print("Response Content: ", response.content)
# # print("parsed Response Content: ", parser.parse(response.content))
