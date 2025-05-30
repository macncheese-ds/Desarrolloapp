class AjustesViewModel:
    def __init__(self):
        self.tema_actual = "claro"

    def cambiar_tema(self, tema):
        self.tema_actual = tema
        return f"theme/{tema}.qss"
