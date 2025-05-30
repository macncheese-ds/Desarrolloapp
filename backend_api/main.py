from fastapi import FastAPI
from routers import diagnosticos, reglas

app = FastAPI()

app.include_router(diagnosticos.router)
app.include_router(reglas.router)

@app.get("/")
def home():
    return {"message": "API de diagnóstico activa"}
