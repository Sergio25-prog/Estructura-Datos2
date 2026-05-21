class NodoPaquete:
    def __init__(self, codigo, origen, destino):
        # Datos del paquete
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.estado = "En Almacén" # Estado por defecto
        
        # Punteros (La clave de la lista doble)
        self.siguiente = None # Apunta al nodo posterior
        self.anterior = None  # Apunta al nodo previo

class ListaDobleLogistica:
    def __init__(self):
        self.cabeza = None # Primer paquete de la lista
        self.cola = None   # Último paquete de la lista

    def esta_vacia(self):
        return self.cabeza is None

    # Operación 1: Insertar al final
    def agregar_paquete(self, codigo, origen, destino):
        nuevo_paquete = NodoPaquete(codigo, origen, destino)
        
        if self.esta_vacia():
            self.cabeza = nuevo_paquete
            self.cola = nuevo_paquete
        else:
            # Conectamos el nuevo paquete al final
            nuevo_paquete.anterior = self.cola
            self.cola.siguiente = nuevo_paquete
            self.cola = nuevo_paquete # El nuevo pasa a ser la cola
        
        print(f"Paquete {codigo} agregado exitosamente.")

    # Operación 2: Buscar paquete
    def buscar_paquete(self, codigo):
        actual = self.cabeza
        while actual:
            if actual.codigo == codigo:
                return actual # Retorna el objeto nodo encontrado
            actual = actual.siguiente
        return None # No se encontró

    # Operación 3: Actualizar estado
    def actualizar_estado(self, codigo, nuevo_estado):
        paquete = self.buscar_paquete(codigo)
        if paquete:
            paquete.estado = nuevo_estado
            print(f"Estado del paquete {codigo} actualizado a: {nuevo_estado}")
        else:
            print("Paquete no encontrado.")

    # Operación 4: Eliminar paquete (Entregado)
    def eliminar_paquete(self, codigo):
        actual = self.buscar_paquete(codigo)
        
        if not actual:
            print("No se puede eliminar: Paquete no encontrado.")
            return

        # Caso 1: Es el único nodo
        if actual == self.cabeza and actual == self.cola:
            self.cabeza = None
            self.cola = None
        
        # Caso 2: Es la cabeza
        elif actual == self.cabeza:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            
        # Caso 3: Es la cola
        elif actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = None
            
        # Caso 4: Está en medio
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            
        print(f"Paquete {codigo} eliminado (Entregado).")

    # Mostrar la lista (Adicional para ver resultados)
    def mostrar_lista(self):
        if self.esta_vacia():
            print("\n--- Lista de Paquetes Vacía ---")
            return
        
        print("\n--- Listado de Paquetes ---")
        actual = self.cabeza
        while actual:
            print(f"[ID: {actual.codigo} | Est: {actual.estado} | {actual.origen} -> {actual.destino}]")
            actual = actual.siguiente
        print("---------------------------\n")


# --- Bloque Principal (Menú) ---
def menu():
    sistema = ListaDobleLogistica()
    
    # Datos de prueba iniciales
    sistema.agregar_paquete("P001", "Madrid", "Barcelona")
    sistema.agregar_paquete("P002", "Valencia", "Sevilla")
    
    while True:
        print("\n=== SISTEMA DE LOGÍSTICA ===")
        print("1. Agregar Paquete")
        print("2. Mostrar Todos")
        print("3. Actualizar Estado")
        print("4. Eliminar Paquete (Entregar)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cod = input("Código: ")
            ori = input("Origen: ")
            des = input("Destino: ")
            sistema.agregar_paquete(cod, ori, des)
        elif opcion == "2":
            sistema.mostrar_lista()
        elif opcion == "3":
            cod = input("Código del paquete a actualizar: ")
            est = input("Nuevo estado: ")
            sistema.actualizar_estado(cod, est)
        elif opcion == "4":
            cod = input("Código del paquete entregado: ")
            sistema.eliminar_paquete(cod)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()