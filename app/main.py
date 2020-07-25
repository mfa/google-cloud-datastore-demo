import uuid

from google.cloud import datastore

from fastapi import FastAPI

app = FastAPI()
datastore_client = datastore.Client()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/demo")
async def demo():
    kind = "Task"
    uid = str(uuid.uuid4())
    task_key = datastore_client.key(kind, uid)

    task = datastore.Entity(key=task_key)
    task["description"] = f"{uid} needs a description"
    datastore_client.put(task)

    # retreive element back and return it
    key = datastore_client.key("Task", uid)
    return datastore_client.get(key)
