# Math Agent

## Purpose
The `math_agent` tool is designed to perform basic arithmetic calculations accurately and efficiently, providing clear and concise answers to the user.

## Capabilities
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Basic order of operations (PEMDAS/BODMAS)

## Accepted Arguments
- `expression` (string): The mathematical expression to evaluate (e.g., "5 + 3 * 2").

## Expected Output
- A JSON object or clear text string containing the calculated numeric result and the original expression.

## Usage Examples

### Example 1: Addition
Input: `expression: "12 + 8"`
Output: `20`

### Example 2: Complex Expression
Input: `expression: "(10 + 5) * 2 - 4"`
Output: `26`