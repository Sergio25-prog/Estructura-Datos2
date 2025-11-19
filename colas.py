from collections import deque
import datetime

class SistemaGestionColas:
    """
    Gestiona múltiples colas de servicio para la administración
    del centro comercial Costa del Mar.
    """
    
    def __init__(self):
        # Usamos un diccionario para manejar las 5 colas departamentales.
        # Cada cola es un objeto 'deque' optimizado.
        self.colas = {
            "tecnologia": deque(),
            "facturacion": deque(),
            "administracion": deque(),
            "mercadeo": deque(),
            "servicios_generales": deque()
        }
        self.contador_solicitudes = 0
        print("Sistema de Gestión de Colas INICIADO.")

    def agregar_solicitud(self, departamento, local, descripcion):
        """
        Operación INSERTAR (Enqueue):
        Agrega una nueva solicitud a la cola del departamento especificado.
        """
        if departamento not in self.colas:
            print(f"Error: El departamento '{departamento}' no existe.")
            return

        # Incrementamos el contador para un ID único
        self.contador_solicitudes += 1
        
        # Creamos la solicitud como un diccionario
        nueva_solicitud = {
            "id": self.contador_solicitudes,
            "local": local,
            "descripcion": descripcion,
            "timestamp": datetime.datetime.now().isoformat(),
            "estado": "pendiente"
        }
        
        # Agregamos la solicitud al final (derecha) de la cola
        self.colas[departamento].append(nueva_solicitud)
        
        print(f"\n[+] Nueva Solicitud (ID: {self.contador_solicitudes}) encolada en '{departamento}'.")
        print(f"    Local: {local} | Problema: {descripcion}")

    def atender_siguiente_solicitud(self, departamento):
        """
        Operación ELIMINAR (Dequeue):
        Remueve y procesa la solicitud al frente de la cola del departamento.
        """
        if departamento not in self.colas:
            print(f"Error: El departamento '{departamento}' no existe.")
            return None

        # Verificamos si la cola tiene solicitudes pendientes
        if not self.colas[departamento]:
            print(f"\n[*] No hay solicitudes pendientes en '{departamento}'.")
            return None

        # Removemos la solicitud del frente (izquierda) de la cola
        solicitud_atendida = self.colas[departamento].popleft()
        
        solicitud_atendida["estado"] = "en_proceso"
        
        print(f"\n[-] Atendiendo Solicitud (ID: {solicitud_atendida['id']}) de '{departamento}'.")
        print(f"    Local: {solicitud_atendida['local']} | Problema: {solicitud_atendida['descripcion']}")
        
        return solicitud_atendida

    def mostrar_estado_colas(self):
        """Helper para visualizar el estado actual de todas las colas."""
        print("\n--- ESTADO ACTUAL DE LAS COLAS ---")
        for depto, cola in self.colas.items():
            print(f"  {depto.capitalize()} ({len(cola)} pendientes): {list(cola)}")
        print("---------------------------------")


# --- Ejemplo de Uso del Sistema ---

# 1. Inicializamos el sistema
sistema = SistemaGestionColas()

# 2. Llegan solicitudes (Insertar / Enqueue)
sistema.agregar_solicitud("tecnologia", "Cine Sala 2", "Proyector no funciona")
sistema.agregar_solicitud("facturacion", "Farmacia Piso 1", "Error en cobro de boleta")
sistema.agregar_solicitud("tecnologia", "Multi-Tienda Piso 3", "Datáfono caído")

# 3. Mostramos el estado
sistema.mostrar_estado_colas()

# 4. El personal atiende solicitudes (Eliminar / Dequeue)
print("\n--- Comienza la atención ---")

# Un técnico de TI se libera
sistema.atender_siguiente_solicitud("tecnologia")

# Un agente de facturación se libera
sistema.atender_siguiente_solicitud("facturacion")

# El mismo técnico de TI se libera de nuevo
sistema.atender_siguiente_solicitud("tecnologia")

# Intentamos atender una cola vacía
sistema.atender_siguiente_solicitud("mercadeo")

# 5. Mostramos el estado final
sistema.mostrar_estado_colas()