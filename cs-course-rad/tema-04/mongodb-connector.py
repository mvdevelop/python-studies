
# mongodb-connector

from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")

    db = client["meubanco"]

    print("Conectado ao MongoDB com sucesso!")

    collections = db.list_collection_names()

    print("Collections existentes:", collections)

except Exception as error:
    print("Erro ao conectar ao MongoDB:", error)
