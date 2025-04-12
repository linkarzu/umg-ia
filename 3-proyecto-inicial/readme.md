# Algoritmo genetico para circuitos Christian Arzu

Programa que aplica un Algoritmo Genético para elegir componentes (resistores,
capacitores, etc.) y formar un circuito con un costo bajo y sin problemas de
voltaje.

## Descripcion General

- **Genera** una población inicial de circuitos aleatorios.
- **Evalúa** cada circuito: calcula un “costo total” y una “penalización” si no
  se cumplen ciertas condiciones de voltaje.
- **Evoluciona** la población a lo largo de varias generaciones, para tratar de
  mejorar los circuitos según el criterio de “fitness”.

Al finalizar, guarda un archivo `resultados.csv` con el mejor circuito de cada
generación.

## Requisitos

- Tener Python 3 instalado.
- No requiere bibliotecas especiales más allá de las que vienen en la
  instalación básica de Python.

## Ejecución

1. Clonar o descargar el repositorio.
2. Abrir la terminal en la carpeta del proyecto.
3. Crear ambiente virtual y ejecutar

```bash
python3 -m venv venv
source venv/bin/activate
python3 circuito_genetico.py
```

4. Observar en la terminal qué tan “bueno” es el mejor circuito en cada
   generación.
5. Revisar el archivo `resultados.csv` para ver el historial de generación,
   mejor fitness y componentes.

## Principales Parámetros

Los parámetros se encuentran en la parte superior del archivo
`circuito_genetico.py`:

- **TAM_POBLACION**  
  Define cuántos circuitos hay en cada generación. Un valor alto implica
  explorar más posibilidades.

- **NUM_GENERACIONES**  
  Indica cuántas veces se repite el proceso de evolución. Un número mayor puede
  dar mejores resultados, pero tomará más iteraciones.

- **TASA_MUTACION**  
  Probabilidad de que un circuito sufra cambios aleatorios.  
  Valores muy altos generan más variación, pero pueden dificultar la estabilidad
  de la población.

## Funcionamiento Interno (Resumen)

1. **Creación de individuos**  
   Se elige aleatoriamente si cada componente (R1, R2, C1, etc.) forma parte del
   circuito o no.

2. **Evaluación (fitness)**  
   Se calcula con esta fórmula (a modo de ejemplo):

   fitness = 1 / (1 + costo_total + penalizacion)

   - `costo_total` se obtiene sumando los costos de los componentes elegidos.
   - `penalizacion` se incrementa si algún componente no soporta el voltaje de
     la fuente.
   - Se puede penalizar el “circuito vacío” agregando un término extra si no se
     incluyen componentes.

3. **Selección, Cruce y Mutación**

   - **Selección**: elige circuitos en función de su fitness (ruleta).
   - **Cruce**: combina componentes del padre y la madre para crear nuevos
     circuitos (hijos).
   - **Mutación**: agrega o quita componentes con una probabilidad definida por
     `TASA_MUTACION`.

4. **Bucle de generaciones**
   - Se repite la evaluación, selección, cruce y mutación hasta llegar al número
     de generaciones definido.

## Archivo de Resultados (CSV)

El archivo `resultados.csv` tiene tres columnas:

- **Generacion**: el número de cada generación (iniciando en 0).
- **Mejor Fitness**: el fitness más alto encontrado en esa generación.
- **Mejor Circuito**: la lista de nombres de componentes que produce ese
  fitness.

## Consejos para Modificar

- **Cambiar la lista de COMPONENTES**: Se pueden añadir más resistores,
  capacitores o cualquier otro elemento (por ejemplo, inductores), ajustando su
  costo, resistencia, capacitancia y voltaje máximo.
- **Modificar la función `evaluar`**: Si se necesita otro criterio (por ejemplo,
  límite de presupuesto o número mínimo de componentes), se puede sumar
  penalizaciones adicionales o cambiar la forma de calcular el fitness.
- **Asegurar que haya fuente**: Si siempre se quiere incluir una fuente, se
  puede obligar su presencia en `crear_individuo()` o penalizar cuando no
  exista.

Este programa sirve como punto de partida para quien quiera probar la aplicación
de Algoritmos Genéticos a la selección de componentes en un circuito.
