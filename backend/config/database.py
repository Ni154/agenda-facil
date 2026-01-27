from pymongo import MongoClient

# URI do MongoDB (local)
MONGO_URI = "mongodb://localhost:27017/"

# Nome do banco
DB_NAME = "agenda_facil"

# Cliente Mongo
client = MongoClient(MONGO_URI)

# Banco de dados
db = client[DB_NAME]

# Coleções (centralizadas)
clientes_collection = db["clientes"]
produtos_collection = db["produtos"]
servicos_collection = db["servicos"]
agendamentos_collection = db["agendamentos"]
vendas_collection = db["vendas"]
despesas_collection = db["despesas"]
