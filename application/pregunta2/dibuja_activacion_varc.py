# dibuja_activacion_varc.py

import os
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mActivación de VarC\033[0m")

# Definir el rango de VarC con puntos clave incluidos
x = np.unique(np.sort(np.concatenate([
    np.linspace(-1.0, 1.0, 102),
    [-0.5, -0.25, 0, 0.25, 0.5]
])))

# Definir funciones de membresía
L = fuzz.trapmf(x, [-1.0, -0.5, -0.25, 0])     # Bajo
M = fuzz.trimf(x, [-0.25, 0, 0.25])            # Medio
H = fuzz.trapmf(x, [0, 0.25, 0.5, 1.0])         # Alto

# Valor de entrada
input_val = -0.2

# Calcular grados de activación
activations = {
    'L': fuzz.interp_membership(x, L, input_val),
    'M': fuzz.interp_membership(x, M, input_val),
    'H': fuzz.interp_membership(x, H, input_val),
}

# Filtrar activaciones no nulas
activations = {k: v for k, v in activations.items() if v > 0}

# Imprimir resultados
print(f"\033[34mActivaciones en VarC = {input_val}\033[0m")
for label, value in activations.items():
    print(f"{label}: {value:.3f}")

# Graficar funciones de membresía
plt.figure(figsize=(8, 5))
plt.plot(x, L, 'g', linewidth=2, label='L')
plt.plot(x, M, 'r', linewidth=2, label='M')
plt.plot(x, H, 'b', linewidth=2, label='H')

# Dibujar líneas horizontales de activación
for label, value in activations.items():
    plt.hlines(value, x[0], x[-1], linestyles='dashed', label=f'{label} corte', alpha=0.6)

# Marcar el valor de entrada
plt.axvline(input_val, color='gray', linestyle='--', label=f'Entrada: {input_val}')

plt.title('Activación de funciones para VarC = -0.2')
plt.xlabel('VarC')
plt.ylabel('Grado de pertenencia')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Crear directorio de salida si no existe
output_dir = 'data/respuesta2'
os.makedirs(output_dir, exist_ok=True)

# Guardar gráfico
output_path = os.path.join(output_dir, 'VarC_activaciones.png')
plt.savefig(output_path)
plt.show()

# Imprimir fin de proceso
print("\033[34mFinalizado...\033[0m \033[33mActivación de VarC\033[0m")
