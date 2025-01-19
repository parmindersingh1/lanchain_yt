from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import ConversationChain
from decouple import config
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.memory import ChatMessageHistory, ConversationBufferMemory, ConversationBufferWindowMemory, ConversationEntityMemory, ConversationSummaryBufferMemory, VectorStoreRetrieverMemory
from langchain_community.vectorstores import Chroma

SECRET_KEY = config('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=SECRET_KEY)

# # ChatMessageHistory
history = ChatMessageHistory()
history.add_user_message("Hi ! there")
history.add_ai_message("Hello whats up")
history.add_user_message("How are you")
history.add_ai_message("I am fine how are you")
# print(history)
print(history.messages)

# # ConversationBufferMemory
# memory = ConversationBufferMemory()
# memory.save_context({"input": "Hello"}, {"output": "Hi whats up"})
# memory.save_context({"input": "how are you"}, {"output": "I am good"})
# # print(memory)
# print(memory.buffer)
# # print(memory.load_memory_variables({}))

# # Using ConversationBufferMemory in Chain
# memory = ConversationBufferMemory()
# conversation = ConversationChain(llm=chat, memory=memory, verbose=True)
# conversation.predict(input="hi there")
# conversation.predict(input="who is virat kohli ?")
# print(memory.buffer)

# # ConversationBufferWindowMemory
# memory = ConversationBufferWindowMemory(k=1)
# memory.save_context({"input": "hi"}, {"output": "whats up"})
# memory.save_context({"input": "not much you"}, {"output": "not much"})
# print(memory.buffer)

# # Using ConversationBufferWindowMemory in Chain
# memory = ConversationBufferWindowMemory(k=1)
# conversation = ConversationChain(llm=chat, memory=memory, verbose=True)
# conversation.predict(input="hi there")
# conversation.predict(input="who is virat kohli ?")
# print(memory.buffer)

# # ConversationEntityMemory
# memory = ConversationEntityMemory(llm=chat)
# conversation = ConversationChain(
#     llm=chat, memory=memory, prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE, verbose=True)
# conversation.predict(input="Rohit & Gill are working on a hackathon project")
# conversation.predict(
#     input="They are trying to add more complex memory structures to Langchain")
# conversation.predict(
#     input="They are adding in a key-value store for entities mentioned so far in the conversation.")
# conversation.predict(input="What do you know about Rohit?")
# # print(memory.buffer)
# print(conversation.memory.entity_store.store)

# # ConversationSummaryBufferMemory
# memory = ConversationSummaryBufferMemory(llm=chat, max_token_limit=50)
# conversation_with_summary = ConversationChain(
#     llm=chat, memory=memory, verbose=True)
# conversation_with_summary.predict(input="Why people are scared of AI?")
# conversation_with_summary.predict(
#     input="What will be impact of AI on Animals?")
# print(memory.load_memory_variables({}))

# # VectorStoreRetrieverMemory
# embedding_function = OpenAIEmbeddings(openai_api_key=SECRET_KEY)
# db = Chroma(embedding_function=embedding_function,
#             persist_directory="./chro_db")
# retriever = db.as_retriever()
# memory = VectorStoreRetrieverMemory(retriever=retriever)
# conversation = ConversationChain(
#     llm=chat, memory=memory, verbose=True)
# conversation.predict(input="Hi, my name is Perry, what's up?")
# conversation.predict(input="My favorite food is pizza")
# conversation.predict(input="My favorite sport is soccer")
# conversation.predict(input="what's my favorite sport?")
