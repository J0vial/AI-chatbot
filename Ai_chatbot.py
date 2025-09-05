client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

# Loop over the user questions
for msg in user_msgs:
    print("User: ", msg)
    
    # Create a dictionary for the user message from q and append to messages
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
