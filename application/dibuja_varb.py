"""
Este script define y grafica funciones de membresía para una variable 'VarB'
en el rango [-1.0, 1.0] utilizando la biblioteca skfuzzy. Las funciones de membresía se definen
de la siguiente manera:

- VL (Muy Bajo): Función trapezoidal con vértices en (-1.0, -1.0, -0.75, -0.5)
- L (Bajo): Función triangular con vértices en (-1.0, -0.25, -0.25, 0)
- M (Medio): Función triangular con vértices en (-0.25, 0, 0, 0.25)
- H (Alto): Función triangular con vértices en (0, 0.25, 0.25, 1.0)
- VH (Muy Alto): Función trapezoidal con vértices en (0.5, 0.75, 1.0, 1.0)

El script genera un gráfico de estas funciones de membresía y lo guarda como un archivo de imagen.

Entradas:
- Ninguna

Salidas:
- Un gráfico de las funciones de membresía guardado como
  'VarB.png' en el directorio 'data/respuesta1'.

Dependencias:
- numpy: Para operaciones numéricas.
- matplotlib: Para graficar las funciones de membresía.
- skfuzzy: Para definir las funciones de membresía difusas.
- os: Para crear directorios y manejar rutas de archivos.

Uso:
Ejecuta el script para generar y guardar el gráfico de las funciones de membresía.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Definimos el rango de VarB
x = np.unique(np.sort(np.concatenate([
    np.linspace(-1.0, 1.0, 102),
    [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]
])))

# Definimos las funciones de membresía
VL = fuzz.trapmf(x, [-1.0, -1.0, -0.75, -0.5])  # Very Low (trapezoidal)
L = fuzz.trimf(x, [-1.0, -0.25, 0])            # Low (triangular)
M = fuzz.trimf(x, [-0.25, 0, 0.25])            # Medium (triangular)
H = fuzz.trimf(x, [0, 0.25, 1.0])              # High (triangular)
VH = fuzz.trapmf(x, [0.5, 0.75, 1.0, 1.0])     # Very High (trapezoidal)

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, VL, 'orange', linewidth=2, label='VL')
plt.plot(x, L, 'g', linewidth=2, label='L')
plt.plot(x, M, 'r', linewidth=2, label='M')
plt.plot(x, H, 'b', linewidth=2, label='H')
plt.plot(x, VH, 'k', linewidth=2, label='VH')

plt.title('Funciones de Membresía de VarB')
plt.xlabel('VarB')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear el directorio si no existe
output_dir = 'data/respuesta1'
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen
output_path = os.path.join(output_dir, 'VarB.png')
plt.savefig(output_path)
plt.show()
