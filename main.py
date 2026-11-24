from src.models.main_agent import chat


def main_agent(user_input: str):
    reponse = chat.send_message(user_input)

    print(reponse.text)
    print("----------------------------------------------")


while True:
    user_input = input("enter your question: ")
    main_agent(user_input)