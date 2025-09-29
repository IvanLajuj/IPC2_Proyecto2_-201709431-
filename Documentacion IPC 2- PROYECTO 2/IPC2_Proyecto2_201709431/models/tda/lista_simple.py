from .nodo import Nodo

class ListaSimple:
    def __init__(self):
        self.primero = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def obtener(self, indice):
        actual = self.primero
        i = 0
        while actual:
            if i == indice:
                return actual.dato
            i += 1
            actual = actual.siguiente
        return None

    def __iter__(self):
        actual = self.primero
        while actual:
            yield actual.dato
            actual = actual.siguiente
