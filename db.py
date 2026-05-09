from pymongo import MongoClient

# Conexión local a MongoDB
cliente = MongoClient("mongodb://localhost:27017/")

# Base de datos del proyecto
db = cliente["tienda_musical_db"]

# Colección principal
coleccion = db["productos_musicales"]