#!/usr/bin/env python3
# ------------------------------------------------------------
# Rutina básica de Algoritmo Genético para optimizar cadenas
# binarias.  Objetivo por defecto: maximizar la cantidad de 1.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Importaciones estándar
# ------------------------------------------------------------
import random
from typing import List, Tuple

# ------------------------------------------------------------
# Parámetros globales
# CAMBIAR ESTOS VALORES PARA OBTENER DIFERENTES RESULTADOS
# ------------------------------------------------------------
# Número de individuos en la población
TAMANO_POBLACION = 30
# Longitud de cada cromosoma (cadena binaria)
LONGITUD_CROMOSOMA = 60
# Cantidad de generaciones
NUM_GENERACIONES = 50
# Probabilidad de cruce
PROB_CRUCE = 0.8
# Probabilidad de mutación por bit
PROB_MUTACION = 0.02


# ------------------------------------------------------------
# Función de aptitud (fitness)
# ------------------------------------------------------------
def aptitud(cromosoma: List[int]) -> int:
    # Suma de los bits: cuenta cuántos 1 contiene
    return sum(cromosoma)


# ------------------------------------------------------------
# Crea un cromosoma aleatorio
# ------------------------------------------------------------
def cromosoma_aleatorio() -> List[int]:
    return [random.randint(0, 1) for _ in range(LONGITUD_CROMOSOMA)]


# ------------------------------------------------------------
# Selección por torneo (k = 3)
# ------------------------------------------------------------
def seleccion_torneo(poblacion: List[List[int]], k: int = 3) -> List[int]:
    contendientes = random.sample(poblacion, k)
    return max(contendientes, key=aptitud)


# ------------------------------------------------------------
# Cruce de un punto
# ------------------------------------------------------------
def cruce(padre1: List[int], padre2: List[int]) -> Tuple[List[int], List[int]]:
    if random.random() > PROB_CRUCE:
        return padre1[:], padre2[:]
    punto = random.randint(1, LONGITUD_CROMOSOMA - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2


# ------------------------------------------------------------
# Mutación bit a bit
# ------------------------------------------------------------
def mutar(cromosoma: List[int]) -> None:
    for i in range(LONGITUD_CROMOSOMA):
        if random.random() < PROB_MUTACION:
            cromosoma[i] ^= 1  # Cambia 0→1 o 1→0


# ------------------------------------------------------------
# Algoritmo Genético principal
# ------------------------------------------------------------
def algoritmo_genetico() -> Tuple[List[int], int]:
    poblacion = [cromosoma_aleatorio() for _ in range(TAMANO_POBLACION)]
    mejor = max(poblacion, key=aptitud)

    for _ in range(NUM_GENERACIONES):
        nueva_poblacion: List[List[int]] = []

        while len(nueva_poblacion) < TAMANO_POBLACION:
            padre1 = seleccion_torneo(poblacion)
            padre2 = seleccion_torneo(poblacion)
            hijo1, hijo2 = cruce(padre1, padre2)
            mutar(hijo1)
            mutar(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion[:TAMANO_POBLACION]
        actual = max(poblacion, key=aptitud)
        if aptitud(actual) > aptitud(mejor):
            mejor = actual

    return mejor, aptitud(mejor)


# ------------------------------------------------------------
# Punto de entrada
# ------------------------------------------------------------
if __name__ == "__main__":
    mejor_cromosoma, mejor_puntaje = algoritmo_genetico()
    print("Mejor cadena encontrada:", "".join(map(str, mejor_cromosoma)))
    print("Puntuación (número de 1):", mejor_puntaje)
