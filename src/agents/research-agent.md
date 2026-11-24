# Research Agent

## Purpose
The `research_agent` is a knowledgeable research tool designed to provide comprehensive, clear, and well-structured explanations and summaries regarding specific persons, companies, concepts, or terms.

## Capabilities
- Synthesizes detailed information about various subjects.
- Handles ambiguous or multi-meaning terms (such as 'Vyzno') by covering the most likely possibilities or exploring what the term might refer to in different contexts.
- Structures findings logically for easy consumption by users and other AI agents.

## Accepted Arguments
- `query` (string): The person, company, concept, or term you want to research.
- `context` (string, optional): Additional contextual information to narrow down the scope of the research.

## Expected Output
A well-formatted Markdown string containing:
1. **Overview/Definition**: A concise summary of the subject.
2. **Key Details**: Important facts, history, features, or characteristics.
3. **Ambiguity Resolution**: If applicable, alternative meanings or potential referents if the term is obscure or multi-faceted.

## Usage Examples

### Example 1: Researching a Specific Concept or Brand
```json
{
  "query": "Vyzno"
}
```
*Output:* A comprehensive breakdown explaining what Vyzno might refer to, detailing any known companies, projects, or conceptual uses associated with the term.

### Example 2: Researching with Context
```json
{
  "query": "Quantum Computing",
  "context": "Focus on recent breakthroughs in error correction"
}
```
*Output:* A structured summary focusing specifically on recent advancements in quantum error correction.