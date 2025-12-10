import networkx as nx
import matplotlib.pyplot as plt

# Función auxiliar para dibujar de forma bonita
def dibujar_grafo(G, pos, titulo, edge_labels=None, node_color='lightblue'):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, 
            node_color=node_color, font_size=10, font_weight='bold', 
            arrows=True, arrowstyle='-|>', arrowsize=20)
     
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    plt.title(titulo)
    plt.axis('off')
    # En un entorno local, usa plt.show() para ver la ventana.
    # Si estás en un notebook (Jupyter/Colab), la imagen aparecerá sola.
    print(f"--> Generando visualización: {titulo}...")
    plt.show() 

# ==========================================
# PARTE 1: ESTRUCTURA DE ÁRBOL (Visualización Jerárquica)
# ==========================================
def simular_arbol_distribucion():
    print("\n--- 1. ÁRBOL DE RUTAS (Jerarquía Logística) ---")
    
    arbol = nx.DiGraph()
    arbol.add_edges_from([
        ("Central", "Norte"), ("Central", "Sur"),
        ("Norte", "Zona_NA"), ("Norte", "Zona_NB"),
        ("Sur", "Zona_SX"), ("Sur", "Zona_SY")
    ])
    
    print("Estructura del Árbol creada.")
    ruta_dfs = list(nx.dfs_preorder_nodes(arbol, source="Central"))
    print(f"Ejemplo de ruta operativa (DFS - Cubrir zona por zona): {ruta_dfs}")
    
    # --- VISUALIZACIÓN DEL ÁRBOL ---
    # Definimos posiciones manuales para que parezca un organigrama jerárquico
    pos = {
        'Central': (0.5, 1.0),
        'Norte': (0.25, 0.7), 'Sur': (0.75, 0.7),
        'Zona_NA': (0.1, 0.4), 'Zona_NB': (0.4, 0.4),
        'Zona_SX': (0.6, 0.4), 'Zona_SY': (0.9, 0.4)
    }
    dibujar_grafo(arbol, pos, "Estructura de Árbol Jerárquico Logístico", node_color='lightgreen')


# ==========================================
# PARTE 2: ESTRUCTURA DE GRAFO (Visualización con Pesos/Tráfico)
# ==========================================
def simular_grafo_trafico():
    print("\n--- 2. GRAFO DE TRÁFICO (Rutas Óptimas con Pesos) ---")
    
    mapa = nx.DiGraph() # Usamos DiGraph para que las flechas se vean claras
    
    # Añadimos conexiones con PESO (minutos de viaje)
    # El ejemplo: El camino directo A->C es lento por tráfico (50 min).
    # El camino indirecto A->B->C es más rápido (10+15 = 25 min).
    mapa.add_edge("Almacen_A", "Punto_B", weight=10)
    mapa.add_edge("Almacen_A", "Cliente_C", weight=50) # Mucho tráfico
    mapa.add_edge("Punto_B", "Cliente_C", weight=15) # Atajo
    mapa.add_edge("Punto_B", "Otro_D", weight=20)
    
    # Cálculo de ruta óptima (Dijkstra)
    ruta_optima = nx.shortest_path(mapa, source="Almacen_A", target="Cliente_C", weight="weight")
    costo_optimo = nx.shortest_path_length(mapa, source="Almacen_A", target="Cliente_C", weight="weight")
    
    print(f"Ruta más rápida calculada (evitando congestión): {ruta_optima}")
    print(f"Tiempo total mínimo: {costo_optimo} minutos")
    
    # --- VISUALIZACIÓN DEL GRAFO ---
    # Usamos un layout automático tipo 'spring' o 'planar'
    pos = nx.planar_layout(mapa) 
    
    # Preparamos las etiquetas de los pesos para dibujarlas
    labels_pesos = nx.get_edge_attributes(mapa, 'weight')
    # Agregamos 'min' al texto para que se entienda en el gráfico
    labels_para_dibujar = {k: f"{v} min" for k, v in labels_pesos.items()}
    
    dibujar_grafo(mapa, pos, "Grafo de Tráfico Ponderado (Pesos = Tiempo)", edge_labels=labels_para_dibujar)


# Ejecución del programa
if __name__ == "__main__":
    # Al ejecutar esto, se abrirán dos ventanas con los gráficos.
    # Cierra la primera ventana para que el programa continúe y muestre la segunda.
    simular_arbol_distribucion()
    simular_grafo_trafico()