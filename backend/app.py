from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.clientes import router as clientes_router
from routes.produtos import router as produtos_router
from routes.servicos import router as servicos_router
from routes.agendamentos import router as agendamentos_router
from routes.vendas import router as vendas_router
from routes.despesas import router as despesas_router
from routes.dashboard import router as dashboard_router
from routes.relatorios import router as relatorios_router
from routes.backup import router as backup_router

app = FastAPI(title="Agenda Fácil API")

# CORS (libera frontend React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(clientes_router, prefix="/api/clientes", tags=["Clientes"])
app.include_router(produtos_router, prefix="/api/produtos", tags=["Produtos"])
app.include_router(servicos_router, prefix="/api/servicos", tags=["Serviços"])
app.include_router(agendamentos_router, prefix="/api/agendamentos", tags=["Agendamentos"])
app.include_router(vendas_router, prefix="/api/vendas", tags=["Vendas"])
app.include_router(despesas_router, prefix="/api/despesas", tags=["Despesas"])
app.include_router(dashboard_router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(relatorios_router, prefix="/api/relatorios", tags=["Relatórios"])
app.include_router(backup_router, prefix="/api/backup", tags=["Backup"])
