# calcular_out.py

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mCálculo de Out - Reglas OR + NOT\033[0m")

# Valores de OutB1
outB1 = {
    'L': 1.0,
    'M': 1.0,
    'H': 0.4472
}

# Valores de VarC
varC = {
    'L': 0.8,
    'M': 0.2,
    'H': 0.0
}

# Valores de VarD
varD = {
    'L': 0.0,
    'M': 0.75,
    'H': 0.25
}

# Definición de reglas (Regla, Antecedentes, Salida)
reglas = [
    ("01", ["OutB1_L", "VarC_L"], "VL"),
    ("02", ["VarC_L", "VarD_M"], "L"),
    ("03", ["OutB1_L", "VarC_L"], "L"),
    ("04", ["OutB1_M", "VarC_M"], "M"),
    ("05", ["OutB1_M", "VarD_M"], "M"),
    ("06", ["VarC_M", "VarD_M"], "M"),
    ("07", ["OutB1_H", "NOT_VarD_L"], "H"),
    ("08", ["VarC_M", "NOT_VarD_H"], "H"),
    ("09", ["NOT_VarC_L", "VarD_H"], "H"),
    ("10", ["OutB1_H", "VarD_H"], "VH")
]

# Colores
GREEN = "\033[92m"
RESET = "\033[0m"

# Funciones auxiliares
def not_yager(valor, w=2):
    return (1 - valor**w)**(1/w)

# Imprimir cabeceras
print(f"{'Regla':<5} {'Antecedentes':<50} {'Out':<15}")
print("-" * 80)

# Procesar y mostrar cada regla
activaciones = {'VL': 0.0, 'L': 0.0, 'M': 0.0, 'H': 0.0, 'VH': 0.0}

for regla in reglas:
    num, antecedentes, salida = regla
    valores = []

    for antecedente in antecedentes:
        if antecedente.startswith("NOT_"):
            var = antecedente[4:]
            nombre, etiqueta = var.split("_")
        else:
            nombre, etiqueta = antecedente.split("_")

        if nombre == "OutB1":
            val = outB1[etiqueta]
        elif nombre == "VarC":
            val = varC[etiqueta]
        elif nombre == "VarD":
            val = varD[etiqueta]
        else:
            val = 0.0

        if antecedente.startswith("NOT_"):
            val = not_yager(val)

        valores.append(val)

    # Aplicar t-conorma (máximo)
    valor_regla = max(valores)

    activaciones[salida] = max(activaciones[salida], valor_regla)

    antecedentes_texto = " OR ".join(antecedentes)
    salida_texto = f"{salida} ({valor_regla:.4f})"

    line = f"{num:<5} {antecedentes_texto:<50} {salida_texto:<15}"

    if valor_regla > 0:
        print(f"{GREEN}{line}{RESET}")
    else:
        print(line)

# Imprimir feedback final
print("\033[34mFinalizado...\033[0m \033[33mCálculo de Out\033[0m")
