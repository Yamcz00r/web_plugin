from fastapi import FastAPI

app = FastAPI()

@app.get('/items/')
def root():
    return {
        "message": "Hello World"
    }