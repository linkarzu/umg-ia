from collections import deque

# Definir el laberinto (0 = camino, 1 = muro)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
]

# Definir puntos de inicio y fin (fila, columna)
inicio = (0, 0)
fin = (4, 4)

# Direcciones posibles: arriba, abajo, izquierda, derecha
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def encontrar_ruta_optima(laberinto, inicio, fin):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Cola para BFS: (fila, columna, camino)
    cola = deque()
    cola.append((inicio[0], inicio[1], []))

    # Celda visitadas
    visitados = set()
    visitados.add((inicio[0], inicio[1]))

    while cola:
        fila, columna, camino = cola.popleft()

        # Verificar si llegamos al final
        if (fila, columna) == fin:
            return camino + [(fila, columna)]

        # Explorar vecinos
        for df, dc in direcciones:
            nfila = fila + df
            ncolumna = columna + dc

            # Validar límites del laberinto
            if 0 <= nfila < filas and 0 <= ncolumna < columnas:
                # Validar si es camino y no ha sido visitado
                if (
                    laberinto[nfila][ncolumna] == 0
                    and (nfila, ncolumna) not in visitados
                ):
                    visitados.add((nfila, ncolumna))
                    cola.append((nfila, ncolumna, camino + [(fila, columna)]))

    return None  # No hay camino posible


# Ejecutar el algoritmo
ruta_optima = encontrar_ruta_optima(laberinto, inicio, fin)

# Mostrar resultados
if ruta_optima:
    print("Ruta óptima encontrada:")
    for paso in ruta_optima:
        print(f"-> {paso}")
else:
    print("No hay ruta posible")
