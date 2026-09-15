from ollama import chat
from ollama import ChatResponse

while True:
        ask = input("Insert questions to ask the model. Type 'exit' to quit: ")

        ask.lower()
        if (ask == "exit"):
                break
        
        response: ChatResponse = chat(model='qwen3:4b', messages=[
        {
            'role': 'user',
            'content': ask,
        },
        ])
        # or access fields directly from the response object
        print(response.message.content)
