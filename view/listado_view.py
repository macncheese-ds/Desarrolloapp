from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton
from viewmodel.listado_viewmodel import ListadoViewModel
from view.agregar_view import AgregarView


class ListadoView(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Listado de Diagnósticos")
        self.setMinimumSize(600, 400)
        self.app = app  # ✅ guardamos la instancia de QApplication

        # Crear layout y widgets
        layout = QVBoxLayout()
        self.label = QLabel("Diagnósticos registrados:")
        self.lista = QListWidget()
        self.btn_ajustes = QPushButton("Ajustes")
        self.btn_ajustes.clicked.connect(self.abrir_ajustes)
        self.btn_agregar = QPushButton("Agregar diagnóstico")
        self.btn_agregar.clicked.connect(self.abrir_agregar)
        layout.addWidget(self.btn_agregar)


        # Agregar widgets al layout
        layout.addWidget(self.label)
        layout.addWidget(self.lista)
        layout.addWidget(self.btn_ajustes)
        self.setLayout(layout)

        # ViewModel y carga de datos
        self.viewmodel = ListadoViewModel()
        self.cargar_diagnosticos()

        # Conectar evento de clic en ítems
        self.lista.itemClicked.connect(self.ver_detalle)

    def cargar_diagnosticos(self):
        diagnosticos = self.viewmodel.obtener_diagnosticos()
        for diag in diagnosticos:
            item = QListWidgetItem(f"{diag.mascota} - {diag.resultado}")
            item.setData(1000, diag)
            self.lista.addItem(item)

    def ver_detalle(self, item):
        diag = item.data(1000)
        print(f"Detalle abierto: {diag.mascota}")
        from view.detalle_view import DetalleView
        self.detalle = DetalleView(diag)
        self.detalle.show()
        self.close()

    def abrir_ajustes(self):
        from view.ajustes_view import AjustesView
        self.ajustes = AjustesView(self.app)
        self.ajustes.show()
    
    def abrir_agregar(self):
        self.agregar = AgregarView(self.app)
        self.agregar.show()

    def cargar_diagnosticos(self):
        self.lista.clear()
        diagnosticos = self.viewmodel.obtener_diagnosticos()
        for diag in diagnosticos:
            item = QListWidgetItem(f"{diag.mascota} - {diag.resultado}")
            item.setData(1000, diag)
            self.lista.addItem(item)

        self.lista.itemClicked.connect(self.ver_detalle)

