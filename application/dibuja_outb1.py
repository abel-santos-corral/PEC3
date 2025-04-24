"""
Este script define y grafica funciones de membresía para la variable 'OutB1'
en el rango [0, 10] usando skfuzzy.

Definiciones:
- L (Bajo): Trapezoidal (0, 0, 3, 7)
- M (Medio): Triangular (4, 5, 6)
- H (Alto): Trapezoidal (4, 7, 10, 10)

Salida:
- Imagen guardada como 'OutB1.png' en 'data/respuesta1'
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Rango extendido con puntos clave
x = np.unique(np.sort(np.concatenate([
    np.linspace(0, 10, 200),
    [0, 3, 4, 5, 6, 7, 10]
])))

# Definición de funciones
L = fuzz.trapmf(x, [0, 0, 3, 7])      # Low
M = fuzz.trimf(x, [4, 5, 6])          # Medium
H = fuzz.trapmf(x, [4, 7, 10, 10])    # High

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, L, 'g', linewidth=2, label='L')
plt.plot(x, M, 'r', linewidth=2, label='M')
plt.plot(x, H, 'b', linewidth=2, label='H')

plt.title('Funciones de Membresía de OutB1')
plt.xlabel('OutB1')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear directorio
output_dir = 'data/respuesta1'
os.makedirs(output_dir, exist_ok=True)

# Guardar imagen
output_path = os.path.join(output_dir, 'OutB1.png')
plt.savefig(output_path)
plt.show()
