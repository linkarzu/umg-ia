#!/usr/bin/env python3

from collections import deque


def bfs_laberinto(laberinto, inicio, meta):
    """
    Realiza una búsqueda en anchura (BFS) para encontrar la ruta más corta
    en un laberinto desde la posición 'inicio' hasta la posición 'meta'.
    Cada movimiento tiene un “costo” de 1 (un salto).

    :param laberinto: Matriz 2D (lista de listas) con 0 = camino libre, 1 = pared/obstáculo
    :param inicio: Tupla (fila, columna) con las coordenadas de inicio
    :param meta: Tupla (fila, columna) con las coordenadas de fin
    :return: Lista de tuplas que representan la ruta más corta, o None si no hay camino
    """
    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Para rastrear la celda de donde venimos y reconstruir ruta
    parent = {}

    # Cola de BFS, empezamos en 'inicio'
    queue = deque([inicio])
    visited = set([inicio])

    # Mientras haya nodos en la cola
    while queue:
        current = queue.popleft()

        # Si llegamos a la meta, reconstruimos la ruta y retornamos
        if current == meta:
            return reconstruir_ruta(parent, inicio, meta)

        # Explorar celdas vecinas
        for mov in movimientos:
            fila_siguiente = current[0] + mov[0]
            col_siguiente = current[1] + mov[1]

            # Verificamos que no nos salgamos del laberinto y que sea camino (0)
            if (
                0 <= fila_siguiente < len(laberinto)
                and 0 <= col_siguiente < len(laberinto[0])
                and laberinto[fila_siguiente][col_siguiente] == 0
            ):
                siguiente = (fila_siguiente, col_siguiente)

                if siguiente not in visited:
                    visited.add(siguiente)
                    parent[siguiente] = current
                    queue.append(siguiente)

    # Si no encontramos ruta, regresamos None
    return None


def reconstruir_ruta(parent, inicio, meta):
    """
    Reconstruye la ruta óptima desde 'meta' hasta 'inicio'
    usando el diccionario 'parent'.
    """
    ruta = []
    actual = meta
    while actual != inicio:
        ruta.append(actual)
        actual = parent[actual]
    ruta.append(inicio)
    ruta.reverse()
    return ruta


def main():
    # Laberinto de ejemplo:
    # 0 = camino, 1 = obstáculo
    laberinto = [
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    inicio = (0, 0)  # Coordenadas (fila, columna) de inicio
    meta = (5, 5)  # Coordenadas (fila, columna) de la meta

    ruta = bfs_laberinto(laberinto, inicio, meta)

    if ruta:
        print("Ruta más corta encontrada:")
        for paso in ruta:
            print(paso)
    else:
        print("No se encontró ninguna ruta posible.")


if __name__ == "__main__":
    main()
