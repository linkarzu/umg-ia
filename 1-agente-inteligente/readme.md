# Tarea Agente Inteligente

## Enunciado tarea

Implementar un Agente Inteligente que recorra de forma autónoma un laberinto, el
recorrido debe de realizarse sobre la ruta optima, debe de utilizar al menos 2
productos de IA, entregable: script en Python y requisitos para su ejecución

## Resolucion con ChatGPT

- En este caso no es necesario utilizar un ambiente virtual `venv` porque no voy
  a estar utilizando paquetes externos adicionales, pero lo voy a crear por
  buena práctica

```bash
python -m venv .venv
source .venv/bin/activate
```

```bash
linkarzu.@.[25/02/14] on  master [?] via 🐍 v3.13.2
~/github/umg-ia/1-agente-inteligente/chatgpt
kubernetes
❯❯❯❯ python -m venv .venv


linkarzu.@.[25/02/14] on  master [?] via 🐍 v3.13.2
~/github/umg-ia/1-agente-inteligente/chatgpt
kubernetes
❯❯❯❯ source .venv/bin/activate
```

- El código utilizado se encuentra en este archivo
  `umg-ia/1-agente-inteligente/chatgpt/agente.py`
- Esta es la matriz utilizada, notar que estamos configurando el punto de inicio
  y la meta (punto final)
- **Cada movimiento tiene un “costo” de 1 (un salto).**

```bash
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
```

- Al ejecutar el archivo de python, este es el resultado obtenido
- Podemos comprobar que la ruta de hecho nos lleva a la meta

```bash
linkarzu.@.[25/02/14] on  master [?] via 🐍 v3.13.2 (.venv)
~/github/umg-ia/1-agente-inteligente/chatgpt
kubernetes
❯❯❯❯ python3 agente.py
Ruta más corta encontrada:
(0, 0)
(1, 0)
(2, 0)
(3, 0)
(3, 1)
(3, 2)
(3, 3)
(4, 3)
(5, 3)
(5, 4)
(5, 5)
```

## Resolucion con DeepSeek

- También utilicé un virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

- Notar la matriz que definimos como laberinto y el punto de inicio y final

```bash
# Definir el laberinto (0 = camino, 1 = muro)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

# Definir puntos de inicio y fin (fila, columna)
inicio = (0, 0)
fin = (4, 4)
```

- Este es el resultado del código ejecutado

```bash
linkarzu.@.[25/02/14] on  master [?] via 🐍 v3.13.2 (.venv)
~/github/umg-ia/1-agente-inteligente/deepseek
kubernetes
❮❮❮❮ python3 agente.py
Ruta óptima encontrada:
-> (0, 0)
-> (1, 0)
-> (2, 0)
-> (3, 0)
-> (4, 0)
-> (4, 1)
-> (4, 2)
-> (4, 3)
-> (4, 4)
```

- Si cambiamos la matriz, notar que encuentra otra ruta

```bash
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
]
```

```bash
linkarzu.@.[25/02/14] on  master [?] via 🐍 v3.13.2 (.venv)
~/github/umg-ia/1-agente-inteligente/deepseek
kubernetes
❮❮❮❮ python3 agente.py
Ruta óptima encontrada:
-> (0, 0)
-> (1, 0)
-> (2, 0)
-> (2, 1)
-> (2, 2)
-> (1, 2)
-> (0, 2)
-> (0, 3)
-> (0, 4)
-> (1, 4)
-> (2, 4)
-> (3, 4)
-> (4, 4)
```
