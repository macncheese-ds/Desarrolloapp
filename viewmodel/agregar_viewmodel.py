from services.api_services import ApiService
from model.diagnostico_model import Diagnostico

class AgregarViewModel:
    def __init__(self):
        self.api = ApiService()

    def predecir_diagnostico(self, sintomas_texto):
        sintomas = [s.strip() for s in sintomas_texto.split(",") if s.strip()]
        return self.api.predecir_diagnostico(sintomas)

    def guardar_diagnostico(self, mascota, sintomas, resultado):
        return self.api.guardar_diagnostico(mascota, sintomas, resultado)
