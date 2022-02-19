from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 2025"}

# to copy updates of this file to a running container, use the following command:
# docker cp main.py b9dc417c8b30:/app/main.py