# dibuja_activacion_vard.py

import os
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Imprimir feedback por pantalla
print("\033[34mEjecutando...\033[0m \033[33mActivación de VarD\033[0m")

# Definir el rango de VarD e incluir puntos clave
x = np.unique(np.sort(np.concatenate([
    np.linspace(-1.0, 1.0, 102),
    [-1.0, -0.8, -0.6, 0.2, 1.0, -0.4]
])))

# Definir funciones de membresía triangulares
L = fuzz.trimf(x, [-1.0, -1.0, -0.8])        # Bajo
M = fuzz.trimf(x, [-0.8, -0.6, 0.2])         # Medio
H = fuzz.trimf(x, [-0.6, 0.2, 1.0])          # Alto

# Valor de entrada
input_val = -0.4

# Calcular grados de activación
activations = {
    'L': fuzz.interp_membership(x, L, input_val),
    'M': fuzz.interp_membership(x, M, input_val),
    'H': fuzz.interp_membership(x, H, input_val),
}

# Filtrar activaciones no nulas
activations = {k: v for k, v in activations.items() if v > 0}

# Mostrar activaciones
print(f"\033[34mActivaciones en VarD = {input_val}\033[0m")
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

plt.title('Activación de funciones para VarD = -0.4')
plt.xlabel('VarD')
plt.ylabel('Grado de pertenencia')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Crear directorio si no existe
output_dir = 'data/respuesta2'
os.makedirs(output_dir, exist_ok=True)

# Guardar gráfico
output_path = os.path.join(output_dir, 'VarD_activaciones.png')
plt.savefig(output_path)
plt.show()

# Imprimir fin de proceso
print("\033[34mFinalizado...\033[0m \033[33mActivación de VarD\033[0m")
