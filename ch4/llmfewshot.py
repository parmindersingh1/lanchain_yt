from langchain_openai import OpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

llm = OllamaLLM(model="llama3.2:latest")

#LLMs
# Few Shot Examples

examples = [
    {
        "input": "The patient presented with acute exacerbation of chronic obstructive pulmonary disease, manifesting symptoms such as dyspnea, increased respiratory rate, and use of accessory muscles for breathing.",

        "output": "The patient is having a sudden worsening of chronic lung disease. This shows with difficulty breathing, faster breathing, and using extra muscles to breathe."
    },
    {
        "input": "The patient is experiencing hyperlipidemia, characterized by elevated levels of low-density lipoprotein cholesterol and triglycerides, along with reduced high-density lipoprotein cholesterol, putting them at increased risk for cardiovascular disease.",

        "output": "The patient has high cholesterol, with too much of the 'bad' kind and triglycerides, and not enough of the 'good' kind. This increases the risk of heart problems."
    }
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"], template="{input}\n{output}"
)

# myprompt = example_prompt.format(**examples[0])
# print(**examples[0])

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="{myinput}",
    input_variables=["myinput"]
)

myprompt = prompt.format(myinput="The patient presented with acute exacerbation of chronic obstructive pulmonary disease, manifesting symptoms such as dyspnea, increased respiratory rate, and use of accessory muscles for breathing.")

# print(myprompt)

response = llm.invoke(myprompt)
print("Response: ", response)