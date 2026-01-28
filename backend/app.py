from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# IMPORTS CORRETOS PARA RENDER (CAMINHO ABSOLUTO)
from backend.routes.cliente import router as cliente_router
from backend.routes.produto import router as produto_router
from backend.routes.servico import router as servico_router
from backend.routes.agendamento import router as agendamento_router
from backend.routes.venda import router as venda_router
from backend.routes.despesa import router as despesa_router
from backend.routes.relatorio import router as relatorio_router

app = FastAPI(
    title="Agenda Fácil API",
    version="1.0.0"
)

# CORS — FRONTEND NO NETLIFY
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://*.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REGISTRO DAS ROTAS
app.include_router(cliente_router, prefix="/api")
app.include_router(produto_router, prefix="/api")
app.include_router(servico_router, prefix="/api")
app.include_router(agendamento_router, prefix="/api")
app.include_router(venda_router, prefix="/api")
app.include_router(despesa_router, prefix="/api")
app.include_router(relatorio_router, prefix="/api")

# HEALTH CHECK
@app.get("/")
def root():
    return {"status": "online"}
