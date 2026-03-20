from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(user_input):
    prompt = f"""
You are a friendly English teacher.

Rules:
- Correct grammar mistakes
- Speak simple English
- If Tamil sentence → translate to English
- Keep answers short

User: {user_input}
Assistant:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


@app.post("/chat")
def chat(msg: str):
    reply = generate_response(msg)
    return {"response": reply}