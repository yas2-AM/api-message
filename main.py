from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Autoriser toutes les origines (temporairement) pour les tests avec Bolt
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Autorise tous les domaines (ex: https://bolt.new)
    allow_credentials=True,      # Important pour que les cookies/autorisations passent
    allow_methods=["*"],         # Autorise toutes les méthodes HTTP (POST, GET…)
    allow_headers=["*"],         # Autorise tous les headers
)

class Message(BaseModel):
    content: str

@app.post("/api/message")
def handle_message(message: Message):
    # On transforme le message reçu en majuscules
    response = message.content.upper()
    return {"response": response}
