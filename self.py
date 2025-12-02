class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_nodo_al_principio(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo

    def agregar_nodo_al_final(self, valor):
        nodo = Nodo(valor)
        if self.cola is None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            self.cola.siguiente = nodo
            nodo.anterior = self.cola
            self.cola = nodo

    def eliminar_nodo(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.cabeza = nodo_actual.siguiente
                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.cola = nodo_actual.anterior
                return
            nodo_actual = nodo_actual.siguiente

    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

# Ejemplo de uso
lista = ListaDoblementeEnlazada()
lista.agregar_nodo_al_final(1)
lista.agregar_nodo_al_final(2)
lista.agregar_nodo_al_final(3)
lista.imprimir_lista()  # Imprime: 1, 2, 3
lista.eliminar_nodo(2)
lista.imprimir_lista()  # Imprime: 1, 3rec