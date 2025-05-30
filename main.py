import sys
from PyQt6.QtWidgets import QApplication
from view.listado_view import ListadoView

class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyle("Fusion")
        self.window = None

    def iniciar_aplicacion(self):
        self.window = ListadoView(self.app)  # Pasamos QApplication para temas
        self.window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    controlador = AppController()
    controlador.iniciar_aplicacion()
