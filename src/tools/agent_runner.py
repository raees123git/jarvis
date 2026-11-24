import os
from config import AGENTS_DIR, MODEL
from src.models.main_agent import client
from google.genai import types

def agent_runner(agent_filename: str, user_task: str) -> str:
    """
    Runs an existing agent to solve the user's task. Call this tool to run an agent with the given filename and user task.

    Args:
        agent_filename: The filename of the Markdown tool to use.
        user_task: The user's task or question to be solved by the tool.
    """
    print(f"Running agent '{agent_filename}' for user task: {user_task}")
    agent_filepath = os.path.join(AGENTS_DIR, agent_filename)
    if not os.path.exists(agent_filepath):
        return f"Error: Agent '{agent_filename}' does not exist."

    with open(agent_filepath, "r", encoding="utf-8") as f:
        agent_instructions = f.read()

    response = client.models.generate_content(
        model=MODEL,
        contents=f"Using the following agent instructions:\n{agent_instructions}\n\nSolve the user's task: {user_task}",
        config=types.GenerateContentConfig(
            system_instruction=agent_instructions,
            top_k=2,
            top_p=0.5,
            temperature=0.7,
            response_mime_type="text/plain",
            seed=42,
        ),
    )

    return response.text
