from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToolRequest(BaseModel):
    name: str
    arguments: dict

@app.post("/tools/call")
def call_tool(request: ToolRequest):
    
    if request.name == "get_weather":
        city = request.arguments.get("city")
        
        # Fake weather logic
        weather_data = {
            "Miami": "85°F and sunny",
            "New York": "60°F and cloudy"
        }
        
        return {
            "result": weather_data.get(city, "Weather not found")
        }
    
    return {"error": "Tool not found"}