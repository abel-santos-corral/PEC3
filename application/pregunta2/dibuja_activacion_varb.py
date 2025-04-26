import os
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Definir el rango de VarB
x = np.unique(np.sort(np.concatenate([
    np.linspace(-1.0, 1.0, 102),
    [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]
])))

# Definir las funciones de membresía
VL = fuzz.trapmf(x, [-1.0, -1.0, -0.75, -0.5])
L = fuzz.trimf(x, [-1.0, -0.25, 0])
M = fuzz.trimf(x, [-0.25, 0, 0.25])
H = fuzz.trimf(x, [0, 0.25, 1.0])
VH = fuzz.trapmf(x, [0.5, 0.75, 1.0, 1.0])

# Valor de entrada
input_val = 0.1  # Puedes cambiar este valor para probar otros casos

# Evaluar cada función en el valor de entrada
activations = {
    'VL': fuzz.interp_membership(x, VL, input_val),
    'L': fuzz.interp_membership(x, L, input_val),
    'M': fuzz.interp_membership(x, M, input_val),
    'H': fuzz.interp_membership(x, H, input_val),
    'VH': fuzz.interp_membership(x, VH, input_val),
}

# Filtrar solo las funciones activas (> 0)
activations = {k: v for k, v in activations.items() if v > 0}

# Imprimir los valores de corte
for label, value in activations.items():
    print(f"{label}: {value:.3f}")

# Graficar todas las funciones
plt.figure(figsize=(8, 5))
plt.plot(x, VL, 'orange', linewidth=2, label='VL')
plt.plot(x, L, 'g', linewidth=2, label='L')
plt.plot(x, M, 'r', linewidth=2, label='M')
plt.plot(x, H, 'b', linewidth=2, label='H')
plt.plot(x, VH, 'k', linewidth=2, label='VH')

# Dibujar líneas horizontales de corte
for label, value in activations.items():
    plt.hlines(value, -1.0, 1.0, linestyles='dashed', label=f'{label} corte', alpha=0.6)

# Marcar el valor de entrada
plt.axvline(input_val, color='gray', linestyle='--', label=f'Entrada: {input_val}')

plt.title(f'Activación de funciones para VarB = {input_val}')
plt.xlabel('VarB')
plt.ylabel('Grado de pertenencia')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Crear el directorio si no existe
output_dir = 'data/respuesta2'
os.makedirs(output_dir, exist_ok=True)

# Guardar el gráfico
output_path = os.path.join(output_dir, 'VarB_activaciones.png')
plt.savefig(output_path)
plt.show()
