#!/usr/bin/env python3

import random
import csv

# Parámetros del Algoritmo Genético
TAM_POBLACION = 10
NUM_GENERACIONES = 50
TASA_MUTACION = 0.1

# Tabla de ejemplo
# Cada entrada tiene:
#   nombre, costo, resistencia, capacitancia, voltaje_max, comentario
COMPONENTES = [
    ("R1", 0.50, 100, None, 50, "Resistor estándar"),
    ("R2", 0.70, 220, None, 100, "Baja tolerancia"),
    ("C1", 1.50, None, 0.01, 16, "Capacitor cerámico"),
    ("C2", 2.00, None, 0.001, 10, "Capacitor de alta precisión"),
    ("V1", 5.00, None, None, 5, "Fuente de alimentación"),
    ("R3", 0.50, 10, None, 25, "Resistencia"),
    ("R4", 0.90, 1000, None, 120, "Resistencia"),
]


def crear_individuo():
    """
    Crea un circuito 'básico' escogiendo un subconjunto de componentes
    (o ajustando valores).
    """
    individuo = []
    for comp in COMPONENTES:
        # Decidimos si este componente se incluye en el circuito (1) o no (0)
        usar = random.randint(0, 1)
        if usar == 1:
            individuo.append(comp)
    return individuo


def evaluar(individuo):
    """
    Función de 'fitness'.
    Por ejemplo:
     - Sumar costos de componentes usados.
     - Penalizar si el voltaje de algún componente < voltaje de la fuente.
    """
    # 1) Calcular costo total
    costo_total = sum(comp[1] for comp in individuo)

    # 2) Revisar si hay una fuente y su voltaje
    fuentes = [c for c in individuo if c[0].startswith("V")]
    capacitores_resistores = [
        c for c in individuo if c[0].startswith("R") or c[0].startswith("C")
    ]

    penalizacion = 0
    if len(fuentes) > 0:
        voltaje_fuente = fuentes[0][4]
        for comp in capacitores_resistores:
            voltaje_max_comp = comp[4]
            if voltaje_max_comp is not None and voltaje_max_comp < voltaje_fuente:
                penalizacion += 10

    # (Opcional) Penalizar circuito vacío:
    # if len(individuo) == 0:
    #     penalizacion += 5

    fitness = 1 / (1 + costo_total + penalizacion)
    return fitness


def seleccion_ruleta(poblacion):
    """
    Selección por ruleta: se eligen 2 padres en función de su fitness relativo.
    """
    aptitud_total = sum(evaluar(ind) for ind in poblacion)

    def seleccionar_uno():
        r = random.uniform(0, aptitud_total)
        suma_acumulada = 0
        for ind in poblacion:
            suma_acumulada += evaluar(ind)
            if suma_acumulada >= r:
                return ind
        return poblacion[-1]

    return seleccionar_uno(), seleccionar_uno()


def cruce(padre, madre):
    """
    Combina el circuito del padre y la madre.
    """
    hijo1 = []
    hijo2 = []
    set_padre = {c[0] for c in padre}
    set_madre = {c[0] for c in madre}

    for comp in COMPONENTES:
        # Construcción del hijo1
        if comp[0] in set_padre and random.random() < 0.5:
            hijo1.append(comp)
        elif comp[0] in set_madre:
            hijo1.append(comp)
        # Construcción del hijo2
        if comp[0] in set_madre and random.random() < 0.5:
            hijo2.append(comp)
        elif comp[0] in set_padre:
            hijo2.append(comp)

    return hijo1, hijo2


def mutacion(individuo):
    """
    Incluye o elimina un componente con cierta probabilidad.
    """
    for comp in COMPONENTES:
        if random.random() < TASA_MUTACION:
            if comp in individuo:
                individuo.remove(comp)
            else:
                individuo.append(comp)
    return individuo


def main():
    # Generar población inicial
    poblacion = [crear_individuo() for _ in range(TAM_POBLACION)]

    # lista para guardar resultados de cada generación
    historial = []

    for gen in range(NUM_GENERACIONES):
        fitnesses = [evaluar(ind) for ind in poblacion]
        mejor_fitness = max(fitnesses)
        indice_mejor = fitnesses.index(mejor_fitness)
        mejor_individuo = poblacion[indice_mejor]

        # Imprimir en pantalla
        print(
            f"Generación {gen} -> Mejor fitness: {mejor_fitness:.4f} | "
            f"Circuito: {[c[0] for c in mejor_individuo]}"
        )

        # Guardar en historial
        historial.append([gen, f"{mejor_fitness:.4f}", [c[0] for c in mejor_individuo]])

        # Crear la siguiente población
        nueva_poblacion = []
        while len(nueva_poblacion) < TAM_POBLACION:
            padre, madre = seleccion_ruleta(poblacion)
            hijo1, hijo2 = cruce(padre, madre)
            hijo1 = mutacion(hijo1)
            hijo2 = mutacion(hijo2)
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)
        poblacion = nueva_poblacion[:TAM_POBLACION]

    # Última evaluación
    fitnesses = [evaluar(ind) for ind in poblacion]
    mejor_fitness = max(fitnesses)
    mejor_individuo = poblacion[fitnesses.index(mejor_fitness)]
    print("\n=== RESULTADO FINAL ===")
    print(f"Mejor individuo: {[c[0] for c in mejor_individuo]}")
    print(f"Fitness: {mejor_fitness:.4f}")

    # Guardar la última generación en historial
    historial.append(
        [NUM_GENERACIONES, f"{mejor_fitness:.4f}", [c[0] for c in mejor_individuo]]
    )

    # Escribir a CSV
    with open("resultados.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Generacion", "Mejor Fitness", "Mejor Circuito"])
        for fila in historial:
            escritor.writerow(fila)


if __name__ == "__main__":
    main()
