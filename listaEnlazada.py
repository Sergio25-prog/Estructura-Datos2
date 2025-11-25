class NodoTarea:
    """
    Clase que representa una tarea individual (El Nodo).
    """
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False  # Por defecto, la tarea no está completada
        self.siguiente = None    # Puntero al siguiente nodo

class ListaTareas:
    """
    Clase que gestiona la Lista Enlazada de tareas.
    """
    def __init__(self):
        self.cabeza = None  # Inicialmente la lista está vacía

    # OPERACIÓN 1: INSERCIÓN
    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = NodoTarea(nombre, descripcion)
        if self.cabeza is None:
            self.cabeza = nueva_tarea
            print(f"Tarea '{nombre}' agregada al inicio.")
            return
        
        # Recorrer hasta el final para agregar
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nueva_tarea
        print(f"Tarea '{nombre}' agregada.")

    # OPERACIÓN 2: ACTUALIZACIÓN (Búsqueda + Modificación)
    def marcar_completada(self, nombre_tarea):
        actual = self.cabeza
        encontrado = False
        while actual:
            if actual.nombre == nombre_tarea:
                actual.completada = True
                print(f"Tarea '{nombre_tarea}' marcada como COMPLETADA.")
                encontrado = True
                break
            actual = actual.siguiente
        
        if not encontrado:
            print(f"Error: No se encontró la tarea '{nombre_tarea}'.")

    # OPERACIÓN 3: ELIMINACIÓN
    def eliminar_tarea(self, nombre_tarea):
        actual = self.cabeza
        anterior = None
        encontrado = False

        while actual:
            if actual.nombre == nombre_tarea:
                encontrado = True
                if anterior is None:
                    # Caso: Eliminar la primera tarea (cabeza)
                    self.cabeza = actual.siguiente
                else:
                    # Caso: Eliminar una tarea intermedia o final
                    anterior.siguiente = actual.siguiente
                print(f"Tarea '{nombre_tarea}' eliminada correctamente.")
                break
            
            # Avanzar punteros
            anterior = actual
            actual = actual.siguiente
        
        if not encontrado:
            print(f"Error: No se puede eliminar. La tarea '{nombre_tarea}' no existe.")

    # MÉTODO AUXILIAR: RECORRIDO (Para mostrar la agenda)
    def mostrar_agenda(self):
        print("\n--- AGENDA DEL PROFESOR ÁNGEL ---")
        actual = self.cabeza
        if not actual:
            print("La agenda está vacía.")
        while actual:
            estado = "[X]" if actual.completada else "[ ]"
            print(f"{estado} Tarea: {actual.nombre} | Desc: {actual.descripcion}")
            actual = actual.siguiente
        print("---------------------------------\n")

# --- BLOQUE DE PRUEBA PARA LA TAREA ---

# 1. Instanciamos la lista
agenda_robotica = ListaTareas()

# 2. Agregamos tareas
agenda_robotica.agregar_tarea("Calibrar Sensores", "Revisar sensores de proximidad del robot X1")
agenda_robotica.agregar_tarea("Comprar Cables", "Adquirir cables jumper macho-hembra")
agenda_robotica.agregar_tarea("Actualizar Firmware", "Instalar versión 2.0 en los microcontroladores")

# Mostramos estado inicial
agenda_robotica.mostrar_agenda()

# 3. Marcamos una tarea como completada
agenda_robotica.marcar_completada("Calibrar Sensores")

# 4. Eliminamos una tarea
agenda_robotica.eliminar_tarea("Comprar Cables")

# Mostramos estado final
agenda_robotica.mostrar_agenda()