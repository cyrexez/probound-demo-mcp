import asyncio
from fastapi import FastAPI, Header, HTTPException
from contextlib import asynccontextmanager
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Define how to launch the MCP Server
# Note: In Docker, this path will be relative to the container root
server_params = StdioServerParameters(
    command="python",
    args=["mcp_service/server.py"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to the MCP server using Standard I/O (stdio)
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            app.state.mcp_session = session
            print("Successfully connected to MCP Server")
            yield
    # Connection closes automatically when FastAPI stops

app = FastAPI(lifespan=lifespan)

@app.post("/agent/call")
async def handle_mcp_orchestration():
    session = app.state.mcp_session
    
    # Fire off 5 parallel tool calls using the protocol
    tasks = [
        session.call_tool("execute_integration", arguments={"task_id": i})
        for i in range(5)
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    return {
        "protocol": "MCP 1.0",
        "status": "orchestration_complete",
        "integration_payloads": [str(r) for r in results]
    }