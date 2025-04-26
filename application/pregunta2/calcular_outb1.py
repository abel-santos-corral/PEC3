# Programa para calcular OutB1 en base a reglas usando tnorma/conorma de Yager (w=2)

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mCálculo de OutB1\033[0m")

# Colores
GREEN = "\033[92m"
RESET = "\033[0m"

# Valores de VarA
varA = {
    'VL': 0.0,
    'L': 0.0,
    'M': 0.8,
    'H': 0.2,
    'VH': 0.0,
    'NOT(H)': 0.9797,
    'NOT(VH)': 1.0
}

# Valores de VarB
varB = {
    'VL': 0.0,
    'L': 0.0,
    'M': 0.6,
    'H': 0.4,
    'VH': 0.0,
    'NOT(H)': 0.9165,
    'NOT(VH)': 1.0
}

# t-norma yager
def t_norm_yager(a, b, w=2):
    return max(0, 1 - (( (1 - a)**w + (1 - b)**w )**(1/w)))

# t-conorma yager
def t_conorm_yager(a, b, w=2):
    return min(1, (a**w + b**w)**(1/w))

# Reglas: (nombre regla, operacion, entrada A, entrada B (o None), salida)
reglas = [
    ("01", "OR", "VL", "VL", "L"),
    ("02", "OR", "L", "VL", "L"),
    ("03", "OR", "VL", "L", "L"),
    ("04", "ONLYA", "M", None, "M"),
    ("05", "ONLYB", None, "M", "M"),
    ("06", "OR", "H", "H", "H"),
    ("07", "OR", "VH", "VH", "H"),
    ("08", "OR", "NOT(H)", "NOT(H)", "L"),
    ("09", "AND", "NOT(VH)", "NOT(VH)", "M"),
    ("10", "AND", "NOT(H)", "NOT(H)", "L"),
]

# Calcular y mostrar resultados
print(f"{'Regla':<5} {'VarA':<18} {'VarB':<18} {'OutB1':<10}")
print("-" * 55)

for regla in reglas:
    num, operacion, entradaA, entradaB, salida = regla
    valA = varA[entradaA] if entradaA else None
    valB = varB[entradaB] if entradaB else None

    if operacion == "OR":
        resultado = t_conorm_yager(valA, valB)
    elif operacion == "AND":
        resultado = t_norm_yager(valA, valB)
    elif operacion == "ONLYA":
        resultado = valA  # Sólo depende de VarA
    elif operacion == "ONLYB":
        resultado = valB  # Sólo depende de VarB
    else:
        resultado = None

    varA_texto = f"{entradaA} ({valA:.4f})" if entradaA else "-"
    varB_texto = f"{entradaB} ({valB:.4f})" if entradaB else "-"
    line =  f"{num:<5} {varA_texto:<18} {varB_texto:<18} {salida} ({resultado:.4f})"

    if resultado > 0:
        print(f"{GREEN}{line}{RESET}")
    else:
        print(line)

# Imprimir feedback por pantalla:
print("\033[34mFinalizado...\033[0m \033[33mCálculo de OutB1\033[0m")
