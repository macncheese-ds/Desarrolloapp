from services.api_services import ApiService
from model.diagnostico_model import Diagnostico

class ListadoViewModel:
    def __init__(self):
        self.api = ApiService()

    def obtener_diagnosticos(self):
        datos = self.api.obtener_diagnosticos()
        diagnosticos = []
        for d in datos:
            diagnosticos.append(Diagnostico(
                d.get("id", 0),
                d.get("mascota", "Sin nombre"),
                d.get("sintomas", ""),
                d.get("resultado", "")
            ))
        return diagnosticos
