# Sistema de Gestión de Logística - Listas Doblemente Enlazadas

Este proyecto implementa un sistema básico de gestión y seguimiento de paquetes para una empresa de logística, desarrollado en **Python**. Utiliza la estructura de datos de **listas doblemente enlazadas** para organizar los paquetes de manera eficiente, permitiendo una navegación bidireccional y optimización en las operaciones de inserción y eliminación.

El proyecto fue diseñado bajo un entorno académico para demostrar el uso práctico de estructuras de datos dinámicas en la resolución de problemas del mundo real.

## 🚀 Características

El sistema simula la administración de una cola de despacho de camiones o almacenes mediante las siguientes operaciones:
*   **Registrar Paquete (Inserción al final):** Incorpora nuevos paquetes al sistema con su origen y destino.
*   **Buscar por Código:** Localiza un paquete específico de forma secuencial.
*   **Actualizar Estado:** Modifica el estado de entrega (*En Almacén, En Tránsito, etc.*) una vez localizado el paquete.
*   **Eliminar Paquete (Entrega):** Remueve los paquetes entregados de la lista de pendientes de forma eficiente gracias a la doble referencia (`siguiente` y `anterior`).

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto solo necesitas tener instalado **Python 3.x** en tu sistema.

