# -*- coding: utf-8 -*-

"""
Este script de Python implementa un sistema simple de gestión de tareas
utilizando una Pila (Stack) para demostrar su funcionamiento (LIFO).
Responde a la Pregunta 3 de la actividad.
"""

class PilaTareas:
    """
    Representa la pila de tareas pendientes para un miembro del equipo.
    Utiliza una lista de Python, donde:
    - append() simula la operación Push (agregar a la cima).
    - pop() simula la operación Pop (quitar de la cima).
    """

    def __init__(self, miembro):
        """
        Inicializa la pila de tareas para un miembro específico.
        """
        self.miembro = miembro
        self.tareas = []
        print(f"Pila de tareas creada para: {self.miembro}")

    def esta_vacia(self):
        """
        Verifica si la pila de tareas está vacía.
        Retorna True si está vacía, False en caso contrario.
        """
        return len(self.tareas) == 0

    def agregar_tarea(self, tarea):
        """
        Añade una nueva tarea a la cima de la pila (Operación Push).
        """
        self.tareas.append(tarea)
        print(f"[PUSH]   -> Tarea agregada: '{tarea}'")

    def completar_tarea(self):
        """
        Completa (elimina) la tarea más reciente de la cima de la pila (Operación Pop).
        """
        if self.esta_vacia():
            print("[POP]    -> ¡ERROR! No hay tareas pendientes para completar.")
            return None
        else:
            # El método .pop() de las listas de Python elimina y devuelve
            # el último elemento, simulando perfectamente el Pop de una pila.
            tarea_completada = self.tareas.pop()
            print(f"[POP]    -> Tarea completada: '{tarea_completada}'")
            return tarea_completada

    def mostrar_tarea_actual(self):
        """
        Muestra la tarea que está actualmente en la cima de la pila (Operación Peek).
        Esta es la tarea en la que el miembro debería estar trabajando.
        """
        if self.esta_vacia():
            print(f"[PEEK]   -> {self.miembro} no tiene tareas pendientes.")
        else:
            # Accedemos al último elemento de la lista (la cima)
            print(f"[PEEK]   -> Tarea actual: '{self.tareas[-1]}'")

    def mostrar_pila_completa(self):
        """
        Muestra todas las tareas en la pila, desde la cima hasta la base.
        """
        if self.esta_vacia():
            print(f"--- La pila de {self.miembro} está vacía ---")
            return

        print(f"--- Pila de Tareas de {self.miembro} ---")
        print("(Cima)")
        # Iteramos en reversa para mostrar la cima primero (LIFO)
        for tarea in reversed(self.tareas):
            print(f"  - {tarea}")
        print("(Base)")
        print("----------------------------------------")


# --- Demostración del Programa ---
if __name__ == "__main__":
    
    print("Iniciando simulación de gestión de tareas...\n")
    
    # 1. Creamos una pila de tareas para un desarrollador
    pila_dev_ana = PilaTareas("Ana García")
    print("-" * 30)

    # 2. Ana no tiene tareas al inicio
    pila_dev_ana.mostrar_tarea_actual()
    pila_dev_ana.mostrar_pila_completa()
    print("-" * 30)

    # 3. Se le asignan tareas (Push)
    pila_dev_ana.agregar_tarea("Diseñar la arquitectura de la base de datos")
    pila_dev_ana.agregar_tarea("Desarrollar el endpoint de 'usuarios'")
    
    # 4. Vemos su pila actual
    pila_dev_ana.mostrar_pila_completa()
    pila_dev_ana.mostrar_tarea_actual() # Debería ser "Desarrollar endpoint"
    print("-" * 30)

    # 5. Llega una tarea urgente (interrupción)
    pila_dev_ana.agregar_tarea("CORREGIR BUG URGENTE: El login no funciona")
    
    # 6. Vemos la tarea actual ahora
    pila_dev_ana.mostrar_tarea_actual() # Ahora es el BUG URGENTE
    pila_dev_ana.mostrar_pila_completa()
    print("-" * 30)

    # 7. Ana completa la tarea actual (Pop)
    pila_dev_ana.completar_tarea() # Completa el BUG
    
    # 8. Vemos qué tarea sigue
    pila_dev_ana.mostrar_tarea_actual() # Vuelve a ser "Desarrollar endpoint"
    pila_dev_ana.mostrar_pila_completa()
    print("-" * 30)

    # 9. Ana completa el resto de sus tareas (Pop, Pop)
    pila_dev_ana.completar_tarea() # Completa "Desarrollar endpoint"
    pila_dev_ana.completar_tarea() # Completa "Diseñar BD"
    
    # 10. La pila queda vacía
    pila_dev_ana.mostrar_pila_completa()
    print("-" * 30)

    # 11. Intentamos completar una tarea de una pila vacía
    pila_dev_ana.completar_tarea() # Debería mostrar el error