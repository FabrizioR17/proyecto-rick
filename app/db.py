from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)

db= cliente['baserick'] #base de datos