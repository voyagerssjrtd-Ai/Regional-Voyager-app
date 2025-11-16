from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TEMP: simulate agent response
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": f"Echo: {req.message}"}
