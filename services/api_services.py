import requests

class ApiService:
    BASE_URL = "https://<TU-BACKEND>.railway.app"  # ⬆️ Reemplaza con tu URL real

    def predecir_diagnostico(self, sintomas_list):
        try:
            response = requests.post(
                f"{self.BASE_URL}/predecir",
                json={"sintomas": sintomas_list}
            )
            if response.status_code == 200:
                return response.json().get("diagnostico", "Desconocido")
            return "Diagnóstico no encontrado"
        except Exception as e:
            return f"Error de conexión: {e}"

    def guardar_diagnostico(self, mascota, sintomas, resultado):
        try:
            response = requests.post(
                f"{self.BASE_URL}/diagnosticos",
                json={
                    "mascota": mascota,
                    "sintomas": sintomas,
                    "resultado": resultado
                }
            )
            return response.status_code == 201
        except Exception as e:
            return False

    def obtener_diagnosticos(self):
        try:
            response = requests.get(f"{self.BASE_URL}/diagnosticos")
            if response.status_code == 200:
                return response.json()  # Lista de dicts
            return []
        except Exception as e:
            return []