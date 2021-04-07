import pymongo
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017/')

db = cliente.dbmidias
colecao = db.posts

print(colecao.find_one({"nome": "Felipe Silva"}))

for item in colecao.find():
    print(item)