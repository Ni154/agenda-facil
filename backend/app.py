import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.settings import settings
from backend.config.database import init_db, Base, engine
from backend.routes import auth, companies, customers, products, suppliers, entries, appointments, sales, nfe, nfse, dashboard, health, cnpj, files

# Create tables on startup (simple bootstrap; for production prefer Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ERP API", version="1.0.0")

# CORS (only allow the provided NETLIFY_URL; fallback to '*')
origins = [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()] or ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(companies.router, prefix="/empresas", tags=["empresas"])
app.include_router(customers.router, prefix="/clientes", tags=["clientes"])
app.include_router(products.router, prefix="/produtos", tags=["produtos"])
app.include_router(suppliers.router, prefix="/fornecedores", tags=["fornecedores"])
app.include_router(entries.router, prefix="/lancamentos", tags=["lancamentos"])
app.include_router(appointments.router, prefix="/agendamentos", tags=["agendamentos"])
app.include_router(sales.router, prefix="/vendas", tags=["vendas"])
app.include_router(nfe.router, prefix="/nfe", tags=["nfe"])
app.include_router(nfse.router, prefix="/nfse", tags=["nfse"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
app.include_router(cnpj.router, prefix="/cnpj", tags=["cnpj"])
app.include_router(files.router, prefix="/files", tags=["files"])

@app.get("/")
def root():
    return {"ok": True, "service": "ERP API", "version": "1.0.0"}
