from google import genai
from google.genai import types
from config import MODEL
from src.prompts.prompt import MAIN_AGENT_PROMPT
from src.models.genai_client import client
from src.tools.tools import tools_list
from dotenv import load_dotenv

load_dotenv()


chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction=MAIN_AGENT_PROMPT,
        tools=tools_list,
    ),
)
