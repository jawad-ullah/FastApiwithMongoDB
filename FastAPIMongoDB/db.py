import pymongo

mongoUrl = "mongodb://localhost:27017/1000"

client = pymongo.MongoClient(mongoUrl)

db = client["TODO"]

collection = db["todo"]

def create(data):
    data =  dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    data = []
    response = collection.find({})
    if response:
        for i in response:
            data.append(str(i["_id"]))
        return data
    else:
        return "Record dose not exist"

def get_one(para):
    response = collection.find_one({"name":para})
    if response:
        response["_id"] =  str(response["_id"])
        return response
    else:
        return "Record dose not exist"

def update(data):
    data = dict(data)
    print(data)
    exist = collection.find_one({"name":data["name"]})
    print(exist)
    if exist:
        response = collection.update_one({"name":data["name"]},{"$set":data})
        return response.modified_count
    else: 
        return "Record dose not eixst"

def delete(name):
    response =  collection.delete_one({"name":name})
    if response:
        return response.deleted_count
    else:
        return "Record dose not exist"