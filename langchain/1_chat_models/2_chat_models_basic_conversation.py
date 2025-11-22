from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


load_dotenv()


model = ChatOpenAI(model = "gpt-4o")

messages = [
    SystemMessage(content = "Solve the following math problem"),
    HumanMessage(content = "Whats 81 divided by 9?")
]

result = model.invoke(messages)

print(result)
print(result.content)

messages = [
    SystemMessage(content = "Solve the following math problem"),
    HumanMessage(content = "Whats 81 divided by 9?"),
    AIMessage(content = "81 divided by 9 is 9"),
    HumanMessage(content = "Whats 10 times 5?"),
]

result = model.invoke(messages)

print(result)
print(result.content)