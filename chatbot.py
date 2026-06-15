def chatbot():
    print("ChatBot: Hello! I'm your basic chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "hello" or user_input == "hi":
            print("ChatBot: Hi!")
            
        elif user_input == "how are you" or user_input == "how are you?":
            print("ChatBot: I'm fine, thanks!")
            
        elif user_input == "bye":
            print("ChatBot: Goodbye!")
            break
            
        elif user_input == "":
            print("ChatBot: Please say something!")
            
        else:
            print("ChatBot: Sorry, I don't understand that. Try 'hello', 'how are you', or 'bye'.")

    chatbot()