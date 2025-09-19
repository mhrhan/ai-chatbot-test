def chatbot_response(msg):
    msg = msg.lower()
    if "hello" in msg:
        return "Hello! How can I help you?"
    elif "bye" in msg:
        return "Goodbye!"
    else:
        return "I don't understand."

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Bot:", chatbot_response(user))
