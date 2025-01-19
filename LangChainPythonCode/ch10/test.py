from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
from decouple import config

SECRET_KEY = config('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=SECRET_KEY)

# Load Document
loader = TextLoader("./data/notes.txt")
mydoc = loader.load()

# Split Document
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
my_document = text_splitter.split_documents(mydoc)

# Embbed Model Object
embedding_function = OpenAIEmbeddings(openai_api_key=SECRET_KEY)

# Store
db = Chroma.from_documents(
    my_document, embedding_function, persist_directory="./chro_db")
db.persist()

# Read from ChromaDB
db_connection = Chroma(embedding_function=embedding_function,
                       persist_directory="./chro_db")

query = "In which date India's Union Budget for the financial year 2024-25 was presented by the Finance Minister Nirmala Sitharaman. ?"

# Compression
compressor = LLMChainExtractor.from_llm(chat)

# Contextual Compression
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=db_connection.as_retriever())

#  Vector Store Retriever
# retriever = db_connection.as_retriever(search_kwargs={"k": 1})
# similar_docs = retriever.get_relevant_documents(query)

similar_docs = compression_retriever.get_relevant_documents(query)
print(similar_docs[0].page_content)
