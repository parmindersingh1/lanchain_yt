from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter, Language, RecursiveCharacterTextSplitter

# # Example 1 - Split by Char
with open("./data/sample.txt") as f:
    sample_data = f.read()

text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=200)

mydata = text_splitter.create_documents([sample_data])
# print(mydata)
# print(mydata[0])
print(mydata[0].page_content)

# Example 2 - Split by Code
# PYTHON_CODE = """
# def hello_world():
#     print("Hello, World!")

# # Call the function
# hello_world()
# """
# python_splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON, chunk_size=100, chunk_overlap=0
# )
# python_docs = python_splitter.create_documents([PYTHON_CODE])
# print(python_docs)
