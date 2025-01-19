from langchain_openai import OpenAIEmbeddings
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
embeddings_model = OpenAIEmbeddings(openai_api_key=SECRET_KEY)

# Embed Query
text = "This is sample text"
embedded_query = embeddings_model.embed_query(text)
# print(embedded_query)

# Embed Document
texts = [
    "Hello Sonam",
    "How are you ?",
    "Where are you now ?"
]

embedded_docs = embeddings_model.embed_documents(texts)
# print(embedded_docs)
print(len(embedded_docs))
