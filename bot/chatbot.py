# Rule-Based Chatbot using if-else

print("Hello! I’m ChatBot. Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        print("Bot: Hello there! How can I help you today?")

    # Asking how bot is
    elif "how are you" in user_input:
        print("Bot: I'm just code, but I'm doing great! Thanks for asking. How about you?")

    # Asking for bot's name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I'm your friendly Python chatbot.")

    # Asking about your day
    elif ("how was your day" in user_input) or ("your day" in user_input):
         print("Bot: My day’s been great, thanks for asking! Just helping people like you.")

    # Asking for help
    elif "help" in user_input or "what can you do" in user_input:
        print("Bot: You can ask me questions, or you can talk to me, or type 'bye' to exit.")

    #feelings
    elif "i am sad" in user_input:
        print("Bot: I’m sorry to hear that. Want to hear a joke to cheer you up?")

    elif "i am happy" in user_input:
        print("Bot: That’s great! Keep smiling.")

    elif "i am angry" in user_input:
        print("Bot: I understand that you're angry. It's okay to feel that way.")

    # Jokes
    elif "joke" in user_input:
        print("Bot: Why was the geometry book so adorable? Because it had acute angles.")

    #fact
    elif "fact" in user_input:
        print("Bot: Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly good to eat!")

    # Goodbye
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    # Thanks
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that. Try typing 'help'.")
