import env
from pymongo import MongoClient


MONGO_URI = env.ATLAS_URL

conn = MongoClient(MONGO_URI)

database = conn["library"]
