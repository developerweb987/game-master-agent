import os
import asyncio
from dotenv import load_dotenv
from game_agents.narrator_agent import NarratorAgent
from game_agents.monster_agent import MonsterAgent
from game_agents.item_agent import ItemAgent
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

narrator_agent = NarratorAgent(model)
monster_agent = MonsterAgent(model)
item_agent = ItemAgent(model)

async def game_loop():
    agent = Agent(
        name="GameMasterAgent",
        instructions=(
            "You run a text-based fantasy adventure game. "
            "Hand off to MonsterAgent for battles and ItemAgent for rewards. "
            "NarratorAgent narrates the story. Only respond with story and actions."
        ),
        handoffs=[narrator_agent, monster_agent, item_agent]
    )

    chat_history = []

    print("Welcome to Game Master Agent! Your adventure begins now.\n")

    while True:
        user_input = input("Your action: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Exiting the adventure. Goodbye!")
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            result = await Runner.run(agent, chat_history, run_config=config)
            response = result.final_output
            print(f"\n{response}\n")
            chat_history.append({"role": "developer", "content": response})
        except Exception as e:
            print(f"Error: {str(e)}\n")


if __name__ == "__main__":
    asyncio.run(game_loop())
