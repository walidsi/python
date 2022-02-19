from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Universe!!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, debug=True)
