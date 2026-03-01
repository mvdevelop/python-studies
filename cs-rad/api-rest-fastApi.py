
# 2️⃣ API REST em minutos com FastAPI - RAD ama frameworks que geram muita coisa automaticamente.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API pronta em segundos!"}

@app.get("/soma")
def soma(a: int, b: int):
    return {"resultado": a + b}

# Rodando: uvicorn main:app --reload
