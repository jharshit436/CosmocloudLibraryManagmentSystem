import env
from pymongo import MongoClient


MONGO_URI = env.MONGO_URI

conn = MongoClient(MONGO_URI)

database = conn["library"]
