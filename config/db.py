from pymongo import MongoClient


MONGO_URI = process.env.MONGO_URL

conn = MongoClient(MONGO_URI)

database = conn["library"]
