from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
# @tool
# def calculator(a:float,b:float) ->str:
#     """Useful for performing basic arithmeric calculations with numbers """
#     print("Tool has been called")
#     return f"la somme de {a} and {b} is {a+b}"

def main():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    tools =[]
    agent_executor=create_react_agent(model,tools)
    print("welcome I am your bot .Type 'quit'  to exit.")
    print("Que puis-je faire pour vous aujourd'hui ?")
    print("Vous pouvez de demander tous ce que vous-voulez")
    while True :
        user_input=input("You :").strip()
        if user_input =='quit':
            break
        print("bot: ",end="")
        for chunk in agent_executor.stream({
        "messages" : [HumanMessage(content=user_input)]}): 
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk['agent']['messages']:
                    print(message.content,end='')
        print()
if __name__ == "__main__":
    main()