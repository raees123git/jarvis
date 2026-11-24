from config import AGENTS_DIR, MODEL
from src.prompts.prompt import MARKDOWN_BUILDER_PROMPT
from src.schemas.agent_markdown import MarkDownFile
from src.models.main_agent import client
from google.genai import types
import os
import json


os.makedirs(AGENTS_DIR, exist_ok=True)


def agent_builder(name: str, instructions: str) -> str:
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
