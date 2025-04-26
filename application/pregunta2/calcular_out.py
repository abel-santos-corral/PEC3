# calcular_out.py

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mCálculo de Out\033[0m")

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

# Definición de reglas (Regla, OutB1, VarC, VarD, Salida)
reglas = [
    ("01", "L", "L", "L", "VL"),
    ("02", "L", "L", "M", "VL"),
    ("03", "L", "L", "H", "L"),
    ("04", "L", "M", "L", "L"),
    ("05", "L", "M", "M", "L"),
    ("06", "L", "M", "H", "M"),
    ("07", "L", "H", "L", "M"),
    ("08", "L", "H", "M", "H"),
    ("09", "L", "H", "H", "VH"),
    ("10", "M", "L", "L", "L"),
    ("11", "M", "L", "M", "M"),
    ("12", "M", "L", "H", "M"),
    ("13", "M", "M", "L", "M"),
    ("14", "M", "M", "M", "M"),
    ("15", "M", "M", "H", "H"),
    ("16", "M", "H", "L", "H"),
    ("17", "M", "H", "M", "H"),
    ("18", "M", "H", "H", "VH"),
    ("19", "H", "L", "L", "L"),
    ("20", "H", "L", "M", "M"),
    ("21", "H", "L", "H", "H"),
    ("22", "H", "M", "L", "M"),
    ("23", "H", "M", "M", "M"),
    ("24", "H", "M", "H", "H"),
    ("25", "H", "H", "L", "H"),
    ("26", "H", "H", "M", "H"),
    ("27", "H", "H", "H", "VH")
]

# Colores
GREEN = "\033[92m"
RESET = "\033[0m"

# Imprimir cabeceras
print(f"{'Regla':<5} {'OutB1':<15} {'VarC':<15} {'VarD':<15} {'Salida':<15}")
print("-" * 65)

# Procesar y mostrar cada regla
for regla in reglas:
    num, entradaB1, entradaC, entradaD, salida = regla
    valB1 = outB1[entradaB1]
    valC = varC[entradaC]
    valD = varD[entradaD]

    # Aplicar t-norma (mínimo)
    valor_regla = min(valB1, valC, valD)

    outB1_texto = f"{entradaB1} ({valB1:.4f})"
    varC_texto = f"{entradaC} ({valC:.4f})"
    varD_texto = f"{entradaD} ({valD:.4f})"
    salida_texto = f"{salida} ({valor_regla:.4f})"

    line = f"{num:<5} {outB1_texto:<15} {varC_texto:<15} {varD_texto:<15} {salida_texto:<15}"

    if valor_regla > 0:
        print(f"{GREEN}{line}{RESET}")
    else:
        print(line)

# Imprimir feedback por pantalla:
print("\033[34mFinalizado...\033[0m \033[33mCálculo de Out\033[0m")
