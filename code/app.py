# main.py
from fastapi import FastAPI
from calculadora import sum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola CI/CD"}

@app.get("/sum")
def calculate_sum(a: float, b: float):
    resultado = sum(a, b)
    return {
        "a": a,
        "b": b,
        "resultado": resultado
    }