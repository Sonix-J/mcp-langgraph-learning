from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My First MCP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result"""
    return a + b

@mcp.tool()
def create_sentence(result: int) -> str:
    """Create a sentence based on the output of the add tool"""
    return f"The result of the addition is {result}."

@mcp.tool()
def get_user_info(name: str, age: int) -> dict:
    """Return user information as a dictionary"""
    return {"user": {"name": name, "age": age}}

@mcp.tool()
def list_of_skills(name: str, skills: list) -> str:
    """Create a list of skills for a user"""
    return f"{name}'s skills are: {', '.join(skills)}."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
