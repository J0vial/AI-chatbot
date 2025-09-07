import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Making demo conversation:
conversation = [
    {
        "role": "system",
        "content": "You are a travel guide designed to provide information about landmarks that tourists should explore in Paris. You speak in a concise manner."
    },
    {
        "role": "user",
        "content": "What is the famous tourist spot in Paris"
    },
    {
        "role": "assistant",
        "content": "The most famous tourist spot in Paris is the Eiffel Tower."
    }
]

# Making chatbots
questions = [
    "How far away is the Louvre from the Eiffel Tower (in driving miles)?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

for qus in questions:
    input_qus = {
        "role": "user",
        "content": qus
    }

    conversation.append(input_qus)

    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )

    print(response.choices[0].message.content)
    conversation.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )
