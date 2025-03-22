# Logica proposicional

## Enunciado

Elaborar un script en Python que evalue la lógica proposicional de una frase /
cadena y que escriba su equivalente (proposicional) en un tabla; entregable:
script de Python

```bash
Crear el entorno virtual
python3 -m venv venv

Activar el entorno virtual En Linux/macOS:
source venv/bin/activate

Instalar pandas
pip install pandas

Guardar las dependencias para compartir o reinstalar fácilmente
pip freeze > requirements.txt

Si quiero instalar este archivo requirements.txt en otro momento
pip install -r requirements.txt
```

## Ejecucion

- Acá muestro la primer ejecución y confirmo que la tabla está correcta

```bash
❯❯❯❯ python3 logica_proposicional.py
=== LÓGICA PROPOSICIONAL ===
Operadores válidos:
- and  → conjunción (y)
- or   → disyunción (o)
- not  → negación (no)
- Usa paréntesis para agrupar expresiones

Ejemplos válidos:
1. p and q
2. not p or r
3. (p or q) and not r
==============================

Ingresa una expresión lógica: p and q and r

✅ Expresión válida. Generando tabla de verdad...

    p     q     r  p and q and r
 True  True  True           True
 True  True False          False
 True False  True          False
 True False False          False
False  True  True          False
False  True False          False
False False  True          False
False False False          False
```

- Una segunda ejecución

```bash
❯❯❯❯ python3 logica_proposicional.py
=== LÓGICA PROPOSICIONAL ===
Operadores válidos:
- and  → conjunción (y)
- or   → disyunción (o)
- not  → negación (no)
- Usa paréntesis para agrupar expresiones

Ejemplos válidos:
1. p and q
2. not p or r
3. (p or q) and not r
==============================

Ingresa una expresión lógica: p or q or r

✅ Expresión válida. Generando tabla de verdad...

    p     q     r  p or q or r
 True  True  True         True
 True  True False         True
 True False  True         True
 True False False         True
False  True  True         True
False  True False         True
False False  True         True
False False False        False
```
