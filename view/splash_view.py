from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer
from viewmodel.splash_viewmodel import SplashViewModel

class SplashView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VetDiag - Cargando")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: white;")
        layout = QVBoxLayout()

        self.label = QLabel("Cargando Diagnóstico de Mascotas...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.viewmodel = SplashViewModel()
        self.start_timer()

    def start_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.launch_main_app)
        timer.start(2000)  # 2 segundos

    def launch_main_app(self):
        print("✅ Splash terminado. Aquí cargaríamos la pantalla de login.")
        self.close()
        # Aquí iría: self.main_window = LoginView() ...
