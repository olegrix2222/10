import pymongo

client = pymongo.MongoClient("mongodb+srv://kkobzar:12345@cluster0.k2acs6d.mongodb.net/?retryWrites=true&w=majority")

db = client["zakhar"]
col = db["zakhar"]

obj = {
  "name":"zakhar"
  "age":120,
  "info":"student"
}

x = col.insert_one(obj)
