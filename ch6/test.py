from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
# from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.document_loaders import TextLoader, CSVLoader, BSHTMLLoader,  PyPDFLoader

from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

chat = ChatOllama(model="llama3.2:latest")

# Examle 1 - Text File
# loader = TextLoader("./data/sample.txt")
# mydata = loader.load()
# print("My Data: ", mydata)
# print("My Data [0]: ", mydata[0])
# print("My Data [0]: \n", mydata[0].page_content)
# print("My MetaData [0]: \n", mydata[0].metadata)

# Example 2 - CSV Loader
# loader = CSVLoader("./data/brand.csv")
# mydata = loader.load()
# print("My Data: ", mydata)
# print("My Data [0]: ", mydata[0])
# print("My Data [0]: \n", mydata[0].page_content)
# print("My MetaData [0]: \n", mydata[0].metadata)

# Example 3 - HTML Loader
# loader = BSHTMLLoader("./data/sample.html")
# mydata = loader.load()
# print("My Data: ", mydata)
# print("My Data [0]: ", mydata[0])
# print("My Data [0]: \n", mydata[0].page_content.replace('\n', ''))
# print("My MetaData [0]: \n", mydata[0].metadata)

# Example 4 - PDF Loader
# loader = PyPDFLoader("./data/sample.pdf")
# mydata = loader.load()
# print("My Data: ", mydata)
# print("My Data [0]: ", mydata[0])
# print("My Data [0]: \n", mydata[0].page_content)
# print("My MetaData [0]: \n", mydata[0].metadata)

# Example 5 - Usage (Legal Advisor)
loader = TextLoader("./data/legal.txt")
my_context =loader.load()[0].page_content
human_template = "{question}\n{company_legal_doc}"
chat_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(human_template)
])
formatted_chat_promt = chat_prompt.format_messages(
    question="How can  iapply for PAN Card",
    company_legal_doc=my_context
)
# print("Formatted Chat Prompt: ", formatted_chat_promt)

response = chat.invoke(formatted_chat_promt)
print("Response ", response.content)