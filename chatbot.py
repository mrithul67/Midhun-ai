# chatbot.py
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def welcome():
    clear()
    print("="*50)
    print("🌟 Welcome to Midhun AI – Your Friendly Chatbot 🌟")
    print("="*50)
    time.sleep(1)

def get_name():
    name = input("👤 What's your name? ")
    slow_print(f"Nice to meet you, {name}! 😊")
    return name

def mood_check():
    mood = input("💬 How are you feeling today? (happy/sad/bored/angry): ").strip().lower()
    responses = {
        "happy": "That's awesome! 😄 Keep shining!",
        "sad": "I'm here for you. Things will get better 🌈",
        "bored": "Let's chat or I can tell you a joke! 🎭",
        "angry": "Take a deep breath. I'm with you 🧘",
    }
    slow_print(responses.get(mood, "I see. I'm always here if you need to talk 💙"))
    return mood

def main_menu():
    while True:
        print("\n🧠 What would you like me to do?")
        print("1. Tell a joke 😂")
        print("2. Give you a quote 📜")
        print("3. Clear screen 🧽")
        print("4. Exit ❌")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            slow_print("Why don’t programmers like nature? It has too many bugs! 🐛")
        elif choice == '2':
            slow_print("“The best way to predict the future is to invent it.” – Alan Kay 💡")
        elif choice == '3':
            clear()
            print("Screen cleared!")
        elif choice == '4':
            slow_print("Goodbye 👋! Midhun AI is always here when you need a friend.")
            break
        else:
            print("Please enter a number between 1 and 4.")

def run_chatbot():
    welcome()
    name = get_name()
    mood_check()
    main_menu()

run_chatbot()
