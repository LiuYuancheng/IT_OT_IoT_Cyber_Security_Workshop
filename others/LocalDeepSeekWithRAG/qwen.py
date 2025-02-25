import asyncio  # Module for asynchronous programming, allowing non-blocking code execution.
import os  # Provides functionality to interact with the operating system.
# debug:https://github.com/browser-use/browser-use/issues/192



from langchain_ollama import ChatOllama  # Importing ChatOllama to interact with the Large Language Model (LLM).
from browser_use import Agent  # Importing Agent to facilitate browser interactions and perform tasks.
os.environ["ANONYMIZED_TELEMETRY"] = "false"
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"
# Define an asynchronous function to perform a browser task using the Agent.
async def run_search():
    # Create an Agent instance configured with a specific task and LLM settings.
    agent = Agent(
        task=(
            # Task description: Navigate to a specific URL and retrieve the page title.
            'Go to https://www.google.com, and search deepseek'
        ),
        llm=ChatOllama(
            # Specify the language model (LLM) to be used by the agent.
            # model='qwen2.5:32b-instruct-q4_K_M', 
            # model='qwen2.5:14b',  
            model='deepseek-r1:1.5b', 
            num_ctx=128000,  # Context length for the model, indicating the amount of information it can process.
        ),
        max_actions_per_step=1,  # Limit the agent to one action per step for controlled operation.
        #tool_call_in_content=False,  # Disables calling tools directly within the content of the task.
    )

    # Execute the agent to perform the defined task.
    await agent.run()

# Main entry point of the script.
if __name__ == '__main__':
    # Use asyncio to run the asynchronous function 'run_search'.
    asyncio.run(run_search())
