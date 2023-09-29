from fastapi import FastAPI
from .models import User

app = FastAPI()

users_db = {}

@app.post("/users/")
def create_user(user: User):
    user_id = len(users_db) + 1
    users_db[user_id] = user.model_dump()
    return {"user_id": user_id}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = users_db.get(user_id)
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        return {"error": "User not found"}
    users_db[user_id] = user.model_dump()
    return {"status": "updated", "user_id": user_id}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        return {"error": "User not found"}
    del users_db[user_id]
    return {"status": "deleted"}
