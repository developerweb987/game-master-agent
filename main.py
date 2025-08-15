import os
import asyncio
from dotenv import load_dotenv

from game_agents.narrator_agent import narrator_agent
from game_agents.monster_agent import monster_agent
from game_agents.item_agent import item_agent

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY missing in .env")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

narrator_agent.model = model
monster_agent.model = model
item_agent.model = model

narrator_agent.handoffs = [monster_agent, item_agent]
monster_agent.handoffs = [item_agent]
item_agent.handoffs = [narrator_agent]

async def game_loop():
    gm = Agent(
        name="GameMasterAgent",
        instructions="Run a simple text adventure using subagents.",
        model=model,
        handoffs=[narrator_agent, monster_agent, item_agent]
    )

    print("\n Game master agent — type commands: explore, attack, defend, run, inventory, quit\n")
    history = []

    while True:
        cmd = input("Action: ").strip()
        if cmd.lower() in ("quit", "exit"):
            print(" Goodbye")
            break

        history.append({"role": "user", "content": cmd})

        try:
            result = await Runner.run(gm, history, run_config=config)
            response = getattr(result, "final_output", str(result))
            print("\n", response, "\n")
            history.append({"role": "assistant", "content": response})
        except Exception as e:
            print(" Error:", e)

if __name__ == "__main__":
    asyncio.run(game_loop())
