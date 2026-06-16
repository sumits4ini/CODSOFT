import datetime
import random

print(" AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey", "good morning", "good evening"]:
        responses = [
            "Hello! How can I help you today?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you?"
        ]
        print("Bot:", random.choice(responses))

    elif "your name" in user_input:
        print("Bot: My name is RuleBot, your virtual assistant.")

    elif "who created you" in user_input:
        print("Bot: I was created by Sumit as part of the CODSOFT AI Internship.")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "what can you do" in user_input:
        print("Bot: I can answer simple questions, tell time and date, and chat with you.")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: The current time is {current_time}")

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    elif "day" in user_input:
        current_day = datetime.datetime.now().strftime("%A")
        print(f"Bot: Today is {current_day}")

    elif "your age" in user_input:
        print("Bot: I don't have an age. I'm a computer program!")

    elif "where are you from" in user_input:
        print("Bot: I live inside your computer.")

    elif "tell me a joke" in user_input:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "tell me a fact" in user_input:
        print("Bot: Python was named after the comedy group 'Monty Python', not the snake.")

    elif "motivate me" in user_input:
        print("Bot: Success comes from consistency, not perfection.")

    elif "quote" in user_input:
        print("Bot: 'The best way to predict the future is to create it.'")

    elif "2+2" in user_input:
        print("Bot: 2 + 2 = 4")

    elif "5*5" in user_input:
        print("Bot: 5 × 5 = 25")

    elif "codsoft" in user_input:
        print("Bot: CODSOFT provides internships in AI, Web Development, Python, and more.")

    elif "internship" in user_input:
        print("Bot: Internships help students gain practical experience and build projects.")

    elif "help" in user_input:
        print("""
Bot: Here are some things you can ask:
- What is your name?
- How are you?
- What can you do?
- Tell me a joke
- Tell me a fact
- Motivate me
- What is the time?
- What is today's date?
- Who created you?
- What is CODSOFT?
- Internship
        """)

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day. 👋")
        break
 
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")