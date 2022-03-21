from nodo import Nodo

class ListaHash:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def listaVacia(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def insertar(self, codigo, nombre):
        elementoInsertar = Nodo(codigo, nombre)
        if self.listaVacia():
            self.primero = self.ultimo = elementoInsertar
        else: 
            self.primero.siguiente = elementoInsertar
            self.ultimo = elementoInsertar
        self.size += 1