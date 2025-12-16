class Vuelo:
    """Clase que representa la información de un vuelo."""
    def __init__(self, numero_vuelo, destino, capacidad):
        self.numero_vuelo = numero_vuelo
        self.destino = destino
        self.capacidad = capacidad
        self.reservas = 0

    def plazas_disponibles(self):
        return self.capacidad - self.reservas

    def __str__(self):
        return f"[Vuelo {self.numero_vuelo}] -> {self.destino} | Libres: {self.plazas_disponibles()}/{self.capacidad}"


class Nodo:
    """Clase que representa un nodo del árbol binario."""
    def __init__(self, vuelo):
        self.vuelo = vuelo
        self.izquierda = None
        self.derecha = None


class SistemaReservas:
    """Clase que gestiona el Árbol Binario de Búsqueda."""
    def __init__(self):
        self.raiz = None

    # --- 1. Inserción (Registrar Vuelo) ---
    def registrar_vuelo(self, numero_vuelo, destino, capacidad):
        nuevo_vuelo = Vuelo(numero_vuelo, destino, capacidad)
        if self.raiz is None:
            self.raiz = Nodo(nuevo_vuelo)
        else:
            self._insertar_recursivo(self.raiz, nuevo_vuelo)
        print(f"Vuelo {numero_vuelo} a {destino} registrado exitosamente.")

    def _insertar_recursivo(self, nodo_actual, nuevo_vuelo):
        if nuevo_vuelo.numero_vuelo < nodo_actual.vuelo.numero_vuelo:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(nuevo_vuelo)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, nuevo_vuelo)
        elif nuevo_vuelo.numero_vuelo > nodo_actual.vuelo.numero_vuelo:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(nuevo_vuelo)
            else:
                self._insertar_recursivo(nodo_actual.derecha, nuevo_vuelo)
        else:
            print("Error: El número de vuelo ya existe.")

    # --- 2. Búsqueda (Buscar Vuelo) ---
    def buscar_vuelo(self, numero_vuelo):
        return self._buscar_recursivo(self.raiz, numero_vuelo)

    def _buscar_recursivo(self, nodo_actual, numero_vuelo):
        if nodo_actual is None:
            return None
        if numero_vuelo == nodo_actual.vuelo.numero_vuelo:
            return nodo_actual
        elif numero_vuelo < nodo_actual.vuelo.numero_vuelo:
            return self._buscar_recursivo(nodo_actual.izquierda, numero_vuelo)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, numero_vuelo)

    # --- 3. Operación de Negocio (Realizar Reserva) ---
    def realizar_reserva(self, numero_vuelo):
        nodo = self.buscar_vuelo(numero_vuelo)
        if nodo:
            if nodo.vuelo.plazas_disponibles() > 0:
                nodo.vuelo.reservas += 1
                print(f"Reserva confirmada en vuelo {numero_vuelo}. Asientos restantes: {nodo.vuelo.plazas_disponibles()}")
            else:
                print(f"Lo sentimos, el vuelo {numero_vuelo} está lleno.")
        else:
            print("Vuelo no encontrado.")

    # --- 4. Operación de Negocio (Cancelar Reserva) ---
    def cancelar_reserva(self, numero_vuelo):
        nodo = self.buscar_vuelo(numero_vuelo)
        if nodo:
            if nodo.vuelo.reservas > 0:
                nodo.vuelo.reservas -= 1
                print(f"Reserva cancelada en vuelo {numero_vuelo}. Asientos restantes: {nodo.vuelo.plazas_disponibles()}")
            else:
                print(f"No hay reservas para cancelar en este vuelo.")
        else:
            print("Vuelo no encontrado.")

    # --- 5. Reporte (Recorrido In-Order) ---
    def generar_informe(self):
        print("\n--- INFORME DE OCUPACIÓN (Ordenado por Nro Vuelo) ---")
        self._inorder_recursivo(self.raiz)
        print("-----------------------------------------------------")

    def _inorder_recursivo(self, nodo):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierda)
            print(nodo.vuelo)
            self._inorder_recursivo(nodo.derecha)

# --- EJECUCIÓN DEL PROGRAMA ---
if __name__ == "__main__":
    sistema = SistemaReservas()

    # 1. Registrar vuelos (ingresados en desorden para probar el árbol)
    sistema.registrar_vuelo(101, "Santiago", 150)
    sistema.registrar_vuelo(50, "Buenos Aires", 100)
    sistema.registrar_vuelo(200, "Lima", 120)
    sistema.registrar_vuelo(75, "Bogotá", 80)

    # 2. Generar informe inicial
    sistema.generar_informe()

    # 3. Realizar operaciones
    print("\n--- Procesando Solicitudes ---")
    sistema.realizar_reserva(101) # Reserva exitosa
    sistema.realizar_reserva(101) # Reserva exitosa
    sistema.realizar_reserva(999) # Vuelo no existe
    sistema.cancelar_reserva(101) # Cancela una

    # 4. Informe final
    sistema.generar_informe()