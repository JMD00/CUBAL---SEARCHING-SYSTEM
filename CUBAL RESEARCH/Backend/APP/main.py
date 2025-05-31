# backend/app/main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.services.varredura import varredura_geral

app = FastAPI(title="API de Varredura e Sondagem de Assuntos")

# Libera acesso CORS para o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def raiz():
    return {"mensagem": "API online. Use /buscar?termo=palavra-chave"}

@app.get("/buscar")
def buscar(termo: str = Query(..., min_length=2, description="Termo de busca")):
    resultados = varredura_geral(termo)
    return {"termo": termo, "resultados": resultados}
