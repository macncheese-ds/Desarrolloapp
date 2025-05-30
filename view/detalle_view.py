from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox
from viewmodel.agregar_viewmodel import AgregarViewModel

class EditarView(QWidget):
    def __init__(self, diagnostico):
        super().__init__()
        self.setWindowTitle("Editar Diagnóstico")
        self.setMinimumSize(400, 300)
        self.diagnostico = diagnostico

        layout = QVBoxLayout()

        self.input_mascota = QLineEdit(diagnostico.mascota)
        self.input_sintomas = QTextEdit(diagnostico.sintomas)
        self.input_resultado = QLineEdit(diagnostico.resultado)

        self.btn_guardar = QPushButton("Guardar cambios")
        self.btn_guardar.clicked.connect(self.guardar)

        layout.addWidget(QLabel("Mascota:"))
        layout.addWidget(self.input_mascota)
        layout.addWidget(QLabel("Síntomas:"))
        layout.addWidget(self.input_sintomas)
        layout.addWidget(QLabel("Resultado:"))
        layout.addWidget(self.input_resultado)
        layout.addWidget(self.btn_guardar)

        self.setLayout(layout)

        self.viewmodel = AgregarViewModel()  # Puedes usar una vista modelo compartida

    def guardar(self):
        mascota = self.input_mascota.text()
        sintomas = self.input_sintomas.toPlainText()
        resultado = self.input_resultado.text()

        if mascota and sintomas and resultado:
            self.diagnostico.mascota = mascota
            self.diagnostico.sintomas = sintomas
            self.diagnostico.resultado = resultado
            print(f"✅ Diagnóstico actualizado: {mascota} → {resultado}")
            QMessageBox.information(self, "Guardado", "Diagnóstico actualizado correctamente.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
