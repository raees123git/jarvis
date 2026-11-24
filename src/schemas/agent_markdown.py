from pydantic import BaseModel, Field

class MarkDownFile(BaseModel):
    name: str = Field(description="The filename ending in .md, e.g., 'calculator-agent.md'")
    description: str = Field(description="The full, detailed Markdown content for the agent")
