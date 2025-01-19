from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
llm = OpenAI(openai_api_key=SECRET_KEY)

# LLMs - Prompt Template

# # Example 1 - Prompt having No Input Variable
noInputPrompt = PromptTemplate(
    input_variables=[], template="Tell me a Python Trick")
# noInputPrompt = PromptTemplate.from_template("Tell me a Python Trick")
formattedNoInputPrompt = noInputPrompt.format()
print("No Input Prompt: ", formattedNoInputPrompt)
# response = llm.invoke(formattedNoInputPrompt)
# print("Response: ", response)

# # Example 2 - Prompt having One Input Variable
# oneInputPrompt = PromptTemplate(
#     input_variables=["language"], template="Tell me a {language} Trick")
# oneInputPrompt = PromptTemplate.from_template("Tell me a {language} Trick")

# formattedOneInputPrompt = oneInputPrompt.format(language="Java")
# print("No Input Prompt: ", formattedOneInputPrompt)
# response = llm.invoke(formattedOneInputPrompt)
# print("Response: ", response)

# # Example 3 - Prompt having Multiple Input Variable
# multipleInputPrompt = PromptTemplate(
#     input_variables=["language", "topic"], template="Tell me a {language} {topic} Trick")
# multipleInputPrompt = PromptTemplate.from_template(
#     "Tell me a {language} {topic} Trick")

# formattedMultipleInputPrompt = multipleInputPrompt.format(
#     language="C Programming", topic="function")
# print("No Input Prompt: ", formattedMultipleInputPrompt)
# response = llm.invoke(formattedMultipleInputPrompt)
# print("Response: ", response)

# Example 4 - PromptTemplate - No input variable manually
# template = "Tell me a {language} {topic} trick"
# promptTemplate = PromptTemplate.from_template(template)
# print("Prompt Template: ", promptTemplate)
# print("Prompt Template Input Variables: ", promptTemplate.input_variables)
# formattedPromptTemplate = promptTemplate.format(
#     language="python",
#     topic="array"
# )
# print("Formatted Prompt Template: ", formattedPromptTemplate)
# response = llm.invoke(formattedPromptTemplate)
# print("Response: ", response)
