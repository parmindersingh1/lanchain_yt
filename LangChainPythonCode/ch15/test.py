from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from decouple import config
HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')

template = "<s>[INST]Write short answer of</s>{question}[/INST]"

prompt_template = PromptTemplate.from_template(template)
formatted_prompt_template = prompt_template.format(
    question="Who was Raja Hari Singh?"
)

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)
# response = llm.invoke(formatted_prompt_template)
# print(response)

# Streaming
response = llm.stream(formatted_prompt_template)
for res in response:
    print(res, end="", flush=True)
