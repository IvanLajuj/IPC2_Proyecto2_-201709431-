from .nodo import Nodo

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.final:
            self.final.siguiente = nuevo
        self.final = nuevo
        if not self.frente:
            self.frente = nuevo

    def desencolar(self):
        if not self.frente:
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        return dato

    def esta_vacia(self):
        return self.frente is None
