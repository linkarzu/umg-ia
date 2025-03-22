import pandas as pd
import itertools
import re


# Mostrar ejemplos y operadores válidos
def mostrar_informacion():
    print("=== LÓGICA PROPOSICIONAL ===")
    print("Operadores válidos:")
    print("- and  → conjunción (y)")
    print("- or   → disyunción (o)")
    print("- not  → negación (no)")
    print("- Usa paréntesis para agrupar expresiones\n")
    print("Ejemplos válidos:")
    print("1. p and q")
    print("2. not p or r")
    print("3. (p or q) and not r")
    print("=" * 30 + "\n")


# Verificar si la expresión solo contiene símbolos válidos
def es_expresion_valida(expr):
    # Solo letras, espacios, paréntesis, and, or, not
    patron = r"^[\s()a-zA-Zandorn]+$"
    if not re.match(patron, expr):
        return False

    # Extraer variables únicas (una sola letra)
    variables = sorted(set(re.findall(r"\b[a-zA-Z]\b", expr)))
    # Crear un diccionario con valores arbitrarios (True)
    valores_ejemplo = {var: True for var in variables}

    try:
        eval_expr(expr, valores_ejemplo)
        return True
    except Exception:
        return False


# Evaluar una expresión usando un diccionario de valores
def eval_expr(expr, valores):
    # Reemplazar variables por sus valores booleanos
    for var in valores:
        expr = re.sub(rf"\b{var}\b", str(valores[var]), expr)
    return eval(expr)


# Generar tabla de verdad
def generar_tabla(expr):
    # Encontrar todas las variables únicas en la expresión
    variables = sorted(set(re.findall(r"\b[a-zA-Z]\b", expr)))
    combinaciones = list(itertools.product([True, False], repeat=len(variables)))

    resultados = []
    for fila in combinaciones:
        valores = dict(zip(variables, fila))
        try:
            resultado = eval_expr(expr, valores)
        except Exception as e:
            resultado = f"ERROR: {e}"
        resultados.append(list(fila) + [resultado])

    columnas = variables + [expr]
    df = pd.DataFrame(resultados, columns=columnas)
    print(df.to_string(index=False))


# Programa principal
if __name__ == "__main__":
    mostrar_informacion()
    expresion = input("Ingresa una expresión lógica: ").strip()

    if not es_expresion_valida(expresion):
        print("❌ La expresión no es válida. Revisa los operadores y paréntesis.")
    else:
        print("\n✅ Expresión válida. Generando tabla de verdad...\n")
        generar_tabla(expresion)
