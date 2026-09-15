from ollama import chat
from ollama import ChatResponse
from tools import soma

while True:
        ask = input("Insert questions to ask the model. Type 'exit' to quit: ")

        if (ask.lower() == "exit"):
                break

        message = [{'role': 'user', 'content': ask}]
        
        response: ChatResponse = chat(model='qwen3:4b', messages=message, tools=[soma], think=True)

        # append in context assistent decision
        message.append(response.message.model_dump())
        
        if(response.message.tool_calls):
                print(response.message.tool_calls)
                call = response.message.tool_calls[0]
                if call.function.name == "soma":
                        result = soma(**call.function.arguments)

                        # Append result for context AI
                        message.append({"role": "tool", "tool_name": call.function.name, "content": str(result)})

                        # Final Response of the all process
                        final_response: ChatResponse = chat(model='qwen3:4b', messages=message, tools=[soma], think=True)


                        print(final_response.message.content)
