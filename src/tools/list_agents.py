import os
from config import AGENTS_DIR


def list_agents() -> list[str]:
    """List all currently available agents saved in the agents folder."""
    print("Listing all available agents...")

    agents = [f for f in os.listdir(AGENTS_DIR) if f.endswith(".md")]

    if agents:
        print("Following agents are found:")
        for agent in agents:
            print(f"- {agent}")
    else:
        print("No agent found.")

    return agents
