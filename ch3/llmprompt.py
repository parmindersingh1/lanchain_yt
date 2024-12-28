from langchain_openai import OpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

llm = OllamaLLM(model="llama3.2:latest")

# LLMS -Prompt Template

# Example 1 - Prompt having No Input Variable
# noInputPrmopt = PromptTemplate(input_variables=[], template="Tell me a Python Trick")
#                                 # or
# # noInputPrmopt = PromptTemplate.from_template("Tell me a Python Trick")
# # print(noInputPrmopt)

# formattedNoInputPrompt = noInputPrmopt.format()
# print("No Input Prompt: " , formattedNoInputPrompt)
# response = llm.invoke(formattedNoInputPrompt)
# print("Response: ", response)

# Example 2 - Prompt having One Input Variable
# oneInputPrmopt = PromptTemplate(input_variables=["language"], template="Tell me a {language} Trick")
#                                 # or
# # oneInputPrmopt = PromptTemplate.from_template("Tell me a {language} Trick")
# # print(oneInputPrmopt)

# formattedOneInputPrompt = oneInputPrmopt.format(language="Javascript")
# print("One Input Prompt: " , formattedOneInputPrompt)
# response = llm.invoke(formattedOneInputPrompt)
# print("Response: ", response)


# Example 3 - Prompt having Multiple Input Variable
# multipleInputPrmopt = PromptTemplate(input_variables=["language", "topic"], template="Tell me a {language} {topic} Trick")
#                                 # or
# # multipleInputPrmopt = PromptTemplate.from_template("Tell me a {language} {topic} Trick")
# # print(multipleInputPrmopt)

# formattedMultipleInputPrompt = multipleInputPrmopt.format(language="Javascript", topic="function")
# print("Multiple Input Prompt: " , formattedMultipleInputPrompt)
# response = llm.invoke(formattedMultipleInputPrompt)
# print("Response: ", response)

# Example 4 - No Input Variable manually
template = "Tell me a {language} {topic} Trick"
promptTemplate = PromptTemplate.from_template(template)
# print("Prompt Template: ", promptTemplate)
# print("Prompt Template Input Variables: ", promptTemplate.input_variables)

formattedPromptTemplate = promptTemplate.format(language="python", topic="array")
# print("Formatted Prompt Template: " , formattedPromptTemplate)
response = llm.invoke(formattedPromptTemplate)
print("Response: ", response)
