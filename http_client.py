import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    async with streamablehttp_client("http://127.0.0.1:8000/mcp") as (
        read_stream, 
        write_stream, 
        _
    ):  # ← 3 values: read_stream, write_stream, and a third one we ignore with _
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            
            tools = await session.list_tools()
            print("Available tools:", tools)
            
            # Call the add tool
            result1 = await session.call_tool("add", arguments={"a": 5, "b": 3})
            print("Result:", result1)

            # Call the create_sentence tool
            result2 = await session.call_tool("create_sentence", arguments={"result": 8})
            print("Sentence:", result2)

            # Call the get_user_info tool
            result3 = await session.call_tool("get_user_info", arguments={"name": "Jayson", "age": 20})
            print("User Info:", result3)

            # Call the list_of_skills tool
            result4 = await session.call_tool("list_of_skills", arguments={"name": "Jayson", "skills": ["React", "Tailwind", "Python"]})
            print("Skills:", result4)

if __name__ == "__main__":
    asyncio.run(main())