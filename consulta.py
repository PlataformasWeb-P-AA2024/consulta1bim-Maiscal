import pymongo
from pymongo import MongoClient

# Conectar a MongoDB
cliente = MongoClient('localhost', 27017)
bd = cliente.consulta_b1
coleccion = bd.atp_tennis

# Realizar la consulta: todos los torneos que ganó Nishikori K. en la primera ronda
consulta = {
    "Winner": "Nishikori K.",
    "Round": "1st Round"
}

# Especificar las columnas que queremos mostrar
proyeccion = {
    "Tournament": 1,
    "Round": 1,
    "Winner": 1,
    "_id": 0  # Excluir el campo _id de la salida
}

resultado_consulta = coleccion.find(consulta, proyeccion)

for documento in resultado_consulta:
    print(documento)