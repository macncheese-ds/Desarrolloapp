from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from viewmodel.ajustes_viewmodel import AjustesViewModel

class AjustesView(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Ajustes")
        self.setMinimumSize(300, 200)
        self.app = app
        self.viewmodel = AjustesViewModel()

        layout = QVBoxLayout()

        label = QLabel("Selecciona el tema:")
        btn_claro = QPushButton("Tema Claro")
        btn_oscuro = QPushButton("Tema Oscuro")

        btn_claro.clicked.connect(lambda: self.aplicar_tema("light"))
        btn_oscuro.clicked.connect(lambda: self.aplicar_tema("dark"))

        layout.addWidget(label)
        layout.addWidget(btn_claro)
        layout.addWidget(btn_oscuro)
        self.setLayout(layout)

    def aplicar_tema(self, tema):
        path = self.viewmodel.cambiar_tema(tema)
        try:
            with open(path, "r") as f:
                estilo = f.read()
                self.app.setStyleSheet(estilo)
                QMessageBox.information(self, "Tema aplicado", f"Tema {tema} aplicado correctamente.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", f"No se encontró el archivo: {path}")
