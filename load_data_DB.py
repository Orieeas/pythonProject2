import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]
with open("employees.json", "r", encoding="utf-8") as file:
    data = json.load(file)
collection.insert_many(data)
client.close()