from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_connection

router = APIRouter()

class DiagnosticoEntrada(BaseModel):
    mascota: str
    sintomas: str
    resultado: str

@router.get("/diagnosticos")
def listar_diagnosticos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, mascota, sintomas, resultado FROM diagnosticos")
    rows = cur.fetchall()
    conn.close()
    return [
        {"id": r[0], "mascota": r[1], "sintomas": r[2], "resultado": r[3]}
        for r in rows
    ]

@router.post("/diagnosticos", status_code=201)
def agregar_diagnostico(d: DiagnosticoEntrada):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO diagnosticos (mascota, sintomas, resultado) VALUES (%s, %s, %s)",
        (d.mascota, d.sintomas, d.resultado)
    )
    conn.commit()
    conn.close()
    return {"message": "Diagnóstico guardado"}
