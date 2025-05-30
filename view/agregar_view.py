from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox
from viewmodel.agregar_viewmodel import AgregarViewModel

class AgregarView(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Agregar Diagnóstico")
        self.setMinimumSize(400, 300)
        self.app = app
        self.viewmodel = AgregarViewModel()

        layout = QVBoxLayout()

        self.input_mascota = QLineEdit()
        self.input_mascota.setPlaceholderText("Nombre de la mascota")

        self.input_sintomas = QTextEdit()
        self.input_sintomas.setPlaceholderText("Síntomas separados por coma")

        self.input_resultado = QLineEdit()
        self.input_resultado.setPlaceholderText("Resultado del diagnóstico")

        self.btn_predecir = QPushButton("Predecir diagnóstico")
        self.btn_predecir.clicked.connect(self.predecir)

        self.btn_guardar = QPushButton("Guardar diagnóstico")
        self.btn_guardar.clicked.connect(self.guardar)

        layout.addWidget(QLabel("Mascota:"))
        layout.addWidget(self.input_mascota)
        layout.addWidget(QLabel("Síntomas:"))
        layout.addWidget(self.input_sintomas)
        layout.addWidget(QLabel("Resultado:"))
        layout.addWidget(self.input_resultado)
        layout.addWidget(self.btn_predecir)
        layout.addWidget(self.btn_guardar)

        self.setLayout(layout)

    def predecir(self):
        sintomas = self.input_sintomas.toPlainText()
        if sintomas:
            resultado = self.viewmodel.predecir_diagnostico(sintomas)
            self.input_resultado.setText(resultado)

    def guardar(self):
        mascota = self.input_mascota.text().strip()
        sintomas = self.input_sintomas.toPlainText().strip()
        resultado = self.input_resultado.text().strip()

        if mascota and sintomas and resultado:
            exito = self.viewmodel.guardar_diagnostico(mascota, sintomas, resultado)
            if exito:
                QMessageBox.information(self, "Guardado", f"Diagnóstico de {mascota} guardado.")
                self.close()
            else:
                QMessageBox.warning(self, "Error", "No se pudo guardar en el backend.")
        else:
            QMessageBox.warning(self, "Error", "Por favor completa todos los campos.")