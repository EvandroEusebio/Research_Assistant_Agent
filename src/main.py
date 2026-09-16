from ollama import chat
from ollama import ChatResponse
from tools import soma, list_file, read_file

while True:
        ask = input("Insert questions to ask the model. Type 'exit' to quit: ")

        if (ask.lower() == "exit"):
                break

        message = [{'role': 'user', 'content': ask}]
        
        response: ChatResponse = chat(model='qwen3:4b', messages=message, tools=[soma, list_file, read_file], think=True)

        # append in context assistent decision
        message.append(response.message.model_dump())
        
        if(response.message.tool_calls):
                # iterate over the tool calls and execute the corresponding functions
                for tool_call in response.message.tool_calls:
                        if(tool_call.function.name == "soma"):
                                result = soma(**tool_call.function.arguments)
                        elif(tool_call.function.name == "list_file"):
                                result = list_file()
                        elif(tool_call.function.name == "read_file"):
                                result = read_file(**tool_call.function.arguments)
                        else:
                                result = "Tool not found"

                        message.append({'role': 'tool', 'tool_name': tool_call.function.name, 'content': str(result)})

                final_response: ChatResponse = chat(model='qwen3:4b', messages=message, tools=[soma, list_file, read_file], think=True)
                print(final_response.message.content)