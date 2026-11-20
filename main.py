from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

AGENTS_DIR = "agents"
os.makedirs(AGENTS_DIR, exist_ok=True)

class MarkDownFile(BaseModel):
    name: str = Field(description="The filename ending in .md, e.g., 'calculator-agent.md'")
    description: str = Field(description="The full, detailed Markdown content for the agent")



MAIN_AGENT_PROMPT = """
You are Jarvis, an orchestrating AI agent.
You manage specialized Markdown tools saved in the tools directory.

Available functions:
1. list_agents: Returns a list of all currently available agents which you can use to perform actions.
2. build_agents: Creates a new agent if a suitable one doesn't exist.
3. agent_runner: Runs an existing agent to solve the user's task.

Workflow:
1. For every user task, first call list_agents.
2. If a suitable agent exists, call agent_runner with its filename and the user's task.
3. If not, call build_agents tool to create one, then call list_agents to get the new agent's filename, and then call agent_runner with that filename.
4. Once agent_runner returns the result, present the final answer clearly to the user.
5. If the user asks a conversational question about YOU, your capabilities, or what tools are available, answer them directly in a friendly manner based on list_agents.
"""

MARKDOWN_BUILDER_PROMPT = """
You are an expert markdown builder engineer. When given a tool name and instructions, thoroughly analyze them and write a detailed Markdown file explaining the tool's purpose, capabilities, accepted arguments, expected output, and usage examples.
This Markdown file will be given to an AI agent as context to solve user questions.

Return your response as a JSON object with:
- "name": a clean kebab-case filename ending in .md (e.g., "calculator-tool.md")
- "description": the full Markdown content of the file.
"""

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



def build_agents(name: str, instructions: str) -> str:
    """
    Creates a new agent with the given name and instructions.

    Args:
        name: Unique descriptive name for the tool.
        instructions: Detailed system instructions for the tool.
    """
    print(f"Building a new agent with name '{name}' and instructions: {instructions}")
    response = client.models.generate_content(
        model=MODEL,
        contents=f"Create a new tool with the name '{name}' and the following instructions: {instructions}",
        config=types.GenerateContentConfig(
            system_instruction=MARKDOWN_BUILDER_PROMPT,
            top_k=2,
            top_p=0.5,
            temperature=0.7,
            response_mime_type="application/json",
            response_schema=MarkDownFile,
            seed=42,
        ),
    )

    data = json.loads(response.text)
    filename = data["name"]
    markdown_content = data["description"]

    if not filename.endswith(".md"):
        filename += ".md"

    filepath = os.path.join(AGENTS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"[SAVED] {filepath}")
    return f"Tool '{filename}' successfully created and saved to {filepath}."


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

tools = [list_agents, build_agents, agent_runner]



chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction=MAIN_AGENT_PROMPT,
        tools=tools,
    ),
)



def main_agent(user_input: str):
    reponse = chat.send_message(user_input)

    print(reponse.text)
    print("----------------------------------------------")


while True:
    user_input = input("enter your question: ")
    main_agent(user_input)