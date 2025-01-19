# from langchain_openai import ChatOpenAI
# from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain.chains import LLMChain
# from decouple import config
# from operator import itemgetter

# SECRET_KEY = config('OPENAI_API_KEY')
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)

# # # Example 1 - Chain
# # human_template = "tell me a fact about {topic}"
# # chat_prompt = ChatPromptTemplate.from_messages([
# #     HumanMessagePromptTemplate.from_template(human_template)
# # ])

# # # chain = LLMChain(llm=chat, prompt=chat_prompt)
# # # chain = chat_prompt | chat
# # chain = chat_prompt | chat | StrOutputParser()

# # # response = chain.invoke(input="javascript")
# # response = chain.invoke({"topic": "python"})
# # print(response)

# # Example 2 - Multiple Chains
# chat_prompt1 = ChatPromptTemplate.from_template(
#     "what is the city {person} is from?")
# chat_prompt2 = ChatPromptTemplate.from_template(
#     "what country is the city {city} in? respond in {language}")

# city_chain = chat_prompt1 | chat | StrOutputParser()

# country_chain = (
#     {"city": city_chain, "language": itemgetter("language")}
#     | chat_prompt2 | chat | StrOutputParser()
# )

# response = country_chain.invoke(
#     {"person": "virat kohli", "language": "english"})

# print(response)
