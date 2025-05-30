from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_connection

router = APIRouter()

class EntradaSintomas(BaseModel):
    sintomas: list

@router.post("/predecir")
def predecir_diagnostico(data: EntradaSintomas):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT sintomas, diagnostico FROM reglas")
    reglas = cur.fetchall()
    conn.close()

    sintomas_usuario = set(s.lower() for s in data.sintomas)

    for sintomas_regla, diagnostico in reglas:
        sintomas_regla = set(s.lower().strip() for s in sintomas_regla.split(","))
        if sintomas_regla.issubset(sintomas_usuario):
            return {"diagnostico": diagnostico}

    raise HTTPException(status_code=404, detail="No se encontró diagnóstico")
