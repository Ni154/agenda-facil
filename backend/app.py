from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔗 IMPORTA TODAS AS ROTAS (AJUSTE NOMES SE NECESSÁRIO)
from routes.cliente import router as cliente_router
from routes.produto import router as produto_router
from routes.servico import router as servico_router
from routes.agendamento import router as agendamento_router
from routes.venda import router as venda_router
from routes.despesa import router as despesa_router
from routes.relatorio import router as relatorio_router

app = FastAPI(
    title="Agenda Fácil API",
    version="1.0.0"
)

# 🔐 CORS — FRONTEND NO NETLIFY
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://*.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🚀 REGISTRO DAS ROTAS
app.include_router(cliente_router)
app.include_router(produto_router)
app.include_router(servico_router)
app.include_router(agendamento_router)
app.include_router(venda_router)
app.include_router(despesa_router)
app.include_router(relatorio_router)

# 🩺 HEALTH CHECK
@app.get("/")
def health():
    return {"status": "online"}
