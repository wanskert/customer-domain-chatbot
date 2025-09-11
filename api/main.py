from fastapi import FastAPI
from pydantic import BaseModel
from src.router_service import RouterService

app = FastAPI(title="Customer Domain Chatbot API")
service = RouterService()

class Msg(BaseModel):
    text: str

@app.post("/classify")
def classify(m: Msg):
    return service.classify(m.text)

@app.post("/chat")
def chat(m: Msg):
    return service.chat(m.text)
