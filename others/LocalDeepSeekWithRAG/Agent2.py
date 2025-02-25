from langchain_ollama import ChatOllama
import os
from browser_use import Agent
import asyncio

import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"
#https://github.com/browser-use/browser-use/issues/442
#https://github.com/browser-use/browser-use/issues/442
async def main():
    try:
        llm = ChatOllama(
            model="deepseek-r1:1.5b",
            num_ctx=32000,
            temperature=0,
            base_url="http://localhost:11434"
        )
        agent = Agent(
            initial_actions=[{"go_to_url": {"url": "https://www.google.com/"}}],
            task="search deepseek",
            use_vision=False,
            #save_conversation_path="logs/conversation",
            llm=llm
        )
        result = await agent.run()
        print(result)
    except Exception as e:
        print(f"Error occurred: {e}")

# Main entry point of the script.
if __name__ == '__main__':
    # Use asyncio to run the asynchronous function 'run_search'.
    asyncio.run(main())
