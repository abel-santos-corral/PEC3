"""
Este script define y grafica funciones de membresía para una variable 'Out'
en el rango [0, 100] utilizando la biblioteca skfuzzy. Las funciones de membresía se definen
como funciones triangulares de la siguiente manera:

- VL (Muy Bajo): (0, 0, 0, 40)
- L (Bajo): (0, 40, 40, 70)
- M (Medio): (40, 70, 70, 90)
- H (Alto): (70, 90, 90, 100)
- VH (Muy Alto): (90, 100, 100, 100)

Entradas:
- Ninguna

Salidas:
- Un gráfico de las funciones de membresía guardado como
  'Out.png' en el directorio 'data/respuesta1'.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Definir rango
x = np.linspace(0, 100, 1001)

# Definir funciones de membresía triangulares
VL = fuzz.trimf(x, [0, 0, 40])
L = fuzz.trimf(x, [0, 40, 70])
M = fuzz.trimf(x, [40, 70, 90])
H = fuzz.trimf(x, [70, 90, 100])
VH = fuzz.trimf(x, [90, 100, 100])

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(x, VL, 'orange', linewidth=2, label='VL')
plt.plot(x, L, 'g', linewidth=2, label='L')
plt.plot(x, M, 'r', linewidth=2, label='M')
plt.plot(x, H, 'b', linewidth=2, label='H')
plt.plot(x, VH, 'k', linewidth=2, label='VH')

plt.title('Funciones de Membresía de Out')
plt.xlabel('Out')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear directorio y guardar imagen
output_dir = 'data/respuesta1'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'Out.png'))
plt.show()
