client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [{"role": "system", "content": "You are a helpful computer science tutor that speaks concisely."}]

print("Chatbot ready! Type 'exit' to stop.\n")

while True:
    # Take input from the user
    msg = input("User: ")
    
    # Exit condition
    if msg.lower() in ["exit", "quit", "stop"]:
        print("Chat ended.")
        break
    
    # Add user input to messages
    user_dict = {"role": "user", "content": msg}
    messages.append(user_dict)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )
    
    # Append the assistant's message to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")
