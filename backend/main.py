from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World"}

@app.get("/users")
def get_users():
    return {"users": []}
