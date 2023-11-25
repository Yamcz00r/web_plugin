from fastapi import FastAPI
import os

app = FastAPI()


db_url = os.getenv("DB_CONNECTION_URL")

@app.get("/")

def read_root():
    return {"db_url": db_url}
