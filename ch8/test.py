from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter, Language, RecursiveCharacterTextSplitter

from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

# chat = ChatOllama(model="llama3.2:latest")
# embeddings_model = OpenAIEmbeddings(open_api_key=SECRET_KEY)
embeddings_model = OllamaEmbeddings(model="llama3.2:latest")

# Embed Query
text = "This is sample text"
embedded_query = embeddings_model.embed_query(text)
# print(embedded_query)

# Embed Document
texts = [
    "Hello Harry Potter",
    "How are you? ",
    "Where is voldemort?"
]

embedded_docs = embeddings_model.embed_documents(texts)

# print(embedded_docs)
print(len(embedded_docs))