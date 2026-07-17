from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CharacterStatus(BaseModel):
    intimacy: int
    days_together: int
    private_chat_count: int


memory = CharacterStatus(       
    intimacy=0,
    days_together=0,
    private_chat_count=0
)

@app.get("/")
def home():
    return {
        "status": "online",
        "project": "Megumi Memory Server"
    }


@app.get("/character/status") 
def get_status():
    return memory