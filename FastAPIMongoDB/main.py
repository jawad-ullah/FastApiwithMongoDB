from urllib import response
from fastapi import FastAPI
import db
from models import Todo

app = FastAPI()

@app.get("/all")
def get_all():
    data =  db.all()
    return {"data": data}

@app.post("/create")
def create(data:Todo):
    id = db.create(data)
    return {"inserted":True , "inserted_id": id}

@app.get("/get")
def get(name:str):
    rec = db.get_one(name)
    return {"rec": rec}
    
@app.get("/delete")
def delete(name: str):
    rec = db.delete(name)
    return {"deleted":True, "deleted_id":rec}

@app.put("/update")
def update(name:str,data:Todo):
    res = db.update(data)
    return {"Updated": True, "Updated_id":res}






