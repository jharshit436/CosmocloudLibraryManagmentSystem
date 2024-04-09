
from pymongo import MongoClient


MONGO_URI = "mongodb+srv://contactjharshit:Harshit123@notetakingapp.5g9ov6g.mongodb.net/?retryWrites=true&w=majority&appName=notetakingapp"

conn = MongoClient(MONGO_URI)

database = conn["library"]
