from langchain_openai import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_community.document_loaders import TextLoader, CSVLoader, BSHTMLLoader, PyPDFLoader

from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=SECRET_KEY)

# Example 1 - Text File
loader = TextLoader("./data/sample.txt")
mydata = loader.load()
print("My Data: ", mydata)
print("My Data [0]: ", mydata[0])
print("My Data [0]:\n", mydata[0].page_content)
print("My Metadata: ", mydata[0].metadata)

# Example 2 - CSV File
# loader = CSVLoader("./data/sample.csv")
# mydata = loader.load()
# print("My Data: ", mydata)
# print("My Data [0]: ", mydata[0])
# print("My Data [0]:\n", mydata[0].page_content)

# Example 3 - HTML File
# loader = BSHTMLLoader("./data/sample.html")
# mydata = loader.load()
# print("My Data: ", mydata)
# print("My Data [0]: ", mydata[0])
# print("My Data [0]:\n", mydata[0].page_content)
# print("My Data [0] Page Content:", mydata[0].page_content.replace('\n', ' '))

# Example 4 - PDF File
# loader = PyPDFLoader("./data/sample.pdf")
# mydata = loader.load()
# print("My Data: ", mydata)
# print("My Data [0]: ", mydata[0])
# print("My Data [0]:\n", mydata[0].page_content)
# print("My Metadata: ", mydata[0].metadata)

# Example 5
# loader = TextLoader("./data/legal.txt")
# my_context = loader.load()[0].page_content
# human_template = "{question}\n{company_legal_doc}"
# chat_prompt = ChatPromptTemplate.from_messages([
#     HumanMessagePromptTemplate.from_template(human_template)
# ])
# fomatted_chat_prompt = chat_prompt.format_messages(
#     question="How can i apply for PAN Card",
#     company_legal_doc=my_context
# )
# # print("Formatted Chat Prompt: ", fomatted_chat_prompt)
# response = chat.invoke(fomatted_chat_prompt)
# print("Response Content: ", response.content)
