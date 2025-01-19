from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

# # Example 1

# # Load Document
# loader = TextLoader('./data/history.txt')
# history_doc = loader.load()

# # Split Document
# text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
# history_document = text_splitter.split_documents(history_doc)

# # Embbed Model Object
# embedding_function = OpenAIEmbeddings(openai_api_key=SECRET_KEY)

# # Store
# db = Chroma.from_documents(history_document, embedding_function)

# query = "The arrival of Islam"

# # similar_docs = db.similarity_search(query)

# #  Vector Store Retriever
# retriever = db.as_retriever()
# similar_docs = retriever.get_relevant_documents(query)
# # print(similar_docs)
# print(similar_docs[0].page_content)


# # Example 2

# # Load Document
# loader = TextLoader('./data/history.txt')
# history_doc = loader.load()

# # Split Document
# text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
# history_document = text_splitter.split_documents(history_doc)

# # Embbed Model Object
# embedding_function = OpenAIEmbeddings(openai_api_key=SECRET_KEY)

# # Store
# db = Chroma.from_documents(
#     history_document, embedding_function, persist_directory="./chro_db")

# db.persist()

# # Read from ChromaDB
# db_connection = Chroma(embedding_function=embedding_function,
#                        persist_directory="./chro_db")

# query = "The arrival of Islam"

# #  Vector Store Retriever
# retriever = db_connection.as_retriever(search_kwargs={"k": 1})
# similar_docs = retriever.get_relevant_documents(query)
# print(similar_docs)

# # Example 2

# Load Document
loader = TextLoader('./data/science.txt')
science_doc = loader.load()

# Split Document
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
science_document = text_splitter.split_documents(science_doc)

# Embbed Model Object
embedding_function = OpenAIEmbeddings(openai_api_key=SECRET_KEY)

# Store
db = Chroma.from_documents(
    science_document, embedding_function, persist_directory="./chro_db")

db.persist()

# Read from ChromaDB
db_connection = Chroma(embedding_function=embedding_function,
                       persist_directory="./chro_db")

query = "The realm of physics"

#  Vector Store Retriever
retriever = db_connection.as_retriever(search_kwargs={"k": 1})
similar_docs = retriever.get_relevant_documents(query)
print(similar_docs)
