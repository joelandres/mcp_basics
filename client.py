import warnings
warnings.filterwarnings("ignore")

import requests

MCP_SERVER = "http://localhost:8000/tools/call"

def call_tool(name, arguments):
    payload = {
        "name": name,
        "arguments": arguments
    }
    
    response = requests.post(MCP_SERVER, json=payload)
    return response.json()

# Simulated model output
model_decision = {
    "tool_call": {
        "name": "get_weather",
        "arguments": {"city": "Miami"}
    }
}

# Execute tool call
result = call_tool(
    model_decision["tool_call"]["name"],
    model_decision["tool_call"]["arguments"]
)

print("Tool result:", result)