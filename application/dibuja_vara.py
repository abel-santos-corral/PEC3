
"""
Este script define y grafica funciones de membresía triangulares para una variable 'VarA'
en el rango [0, 2.0] utilizando la biblioteca skfuzzy. Las funciones de membresía se definen
de la siguiente manera:

- VL (Muy Bajo): Función triangular con vértices en (0, 0, 0.5)
- L (Bajo): Función triangular con vértices en (0, 0.5, 1.0)
- M (Medio): Función triangular con vértices en (0.5, 1.0, 1.5)
- H (Alto): Función triangular con vértices en (1.0, 1.5, 2.0)
- VH (Muy Alto): Función triangular con vértices en (1.5, 2.0, 2.0)

El script genera un gráfico de estas funciones de membresía y lo guarda como un archivo de imagen.

Entradas:
- Ninguna

Salidas:
- Un gráfico de las funciones de membresía guardado como
  'VarA.png' en el directorio 'data/respuesta1'.

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

# Definimos el rango de VarA
x = np.linspace(0, 2.0, 101)

# Definimos las funciones de membresía trapezoidales
VL = fuzz.trimf(x, [0, 0, 0.5])      # Very Low
L = fuzz.trimf(x, [0, 0.5, 1.0])     # Low
M = fuzz.trimf(x, [0.5, 1.0, 1.5])   # Medium
H = fuzz.trimf(x, [1.0, 1.5, 2.0])   # High
VH = fuzz.trimf(x, [1.5, 2.0, 2.0])  # Very High

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, VL, 'orange', linewidth=2, label='VL')
plt.plot(x, L, 'g', linewidth=2, label='L')
plt.plot(x, M, 'r', linewidth=2, label='M')
plt.plot(x, H, 'b', linewidth=2, label='H')
plt.plot(x, VH, 'k', linewidth=2, label='VH')

plt.title('Funciones de Membresía de VarA')
plt.xlabel('VarA')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear el directorio si no existe
output_dir = 'data/respuesta1'
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen
output_path = os.path.join(output_dir, 'VarA.png')
plt.savefig(output_path)
plt.show()
