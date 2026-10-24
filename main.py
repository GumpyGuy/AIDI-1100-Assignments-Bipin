from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add(a: int, b: int):
    result = a + b
    return {"sum": result}
