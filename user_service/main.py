from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "user_service", "status": "up"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "username": "john_doe"}

