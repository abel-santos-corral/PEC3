"""
Este script define y grafica funciones de membresía para una variable 'VarC'
en el rango [-1.0, 1.0] utilizando la biblioteca skfuzzy. Las funciones de membresía se definen
de la siguiente manera:

- L (Bajo): Función trapezoidal con vértices en (-1.0, -0.5, -0.25, 0)
- M (Medio): Función triangular con vértices en (-0.25, 0, 0.25)
- H (Alto): Función trapezoidal con vértices en (0, 0.25, 0.5, 1.0)

El script genera un gráfico de estas funciones de membresía y lo guarda como un archivo de imagen.

Entradas:
- Ninguna

Salidas:
- Un gráfico de las funciones de membresía guardado como
  'VarC.png' en el directorio 'data/respuesta1'.

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

# Definimos el rango de VarC e incluimos puntos clave
x = np.unique(np.sort(np.concatenate([
    np.linspace(-1.0, 1.0, 102),
    [-0.5, -0.25, 0, 0.25, 0.5]
])))

# Definimos las funciones de membresía
L = fuzz.trapmf(x, [-1.0, -0.5, -0.25, 0])     # Low (trapezoidal)
M = fuzz.trimf(x, [-0.25, 0, 0.25])            # Medium (triangular)
H = fuzz.trapmf(x, [0, 0.25, 0.5, 1.0])         # High (trapezoidal)

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, L, 'g', linewidth=2, label='L')
plt.plot(x, M, 'r', linewidth=2, label='M')
plt.plot(x, H, 'b', linewidth=2, label='H')

# Función para anotar pendiente (ahora recibe texto directamente)
def annotate_slope(label_pos, slope_text):
    plt.annotate(slope_text, xy=label_pos, textcoords="offset points",
                 xytext=(0,10), ha='center', fontsize=12, color='black')

# Anotar pendiente de L
annotate_slope((-0.75, 0.2), "2x+2") # posición del texto + pendiente manual
annotate_slope((-0.30, 0.8), "-4x")
# Anotar pendiente de M
annotate_slope((-0.28, 0.2), "4x+1")
annotate_slope((0.28, 0.2), "1-4x")
# Anotar pendiente de H
annotate_slope((0.27, 0.8), "4x")
annotate_slope((0.75, 0.2), "2-2x")

plt.title('Funciones de Membresía de VarC')
plt.xlabel('VarC')
plt.ylabel('Grado de pertenencia')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()

# Ajustar el layout para incluir la leyenda
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Crear el directorio si no existe
output_dir = 'data/respuesta1'
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen
output_path = os.path.join(output_dir, 'VarC.png')
plt.savefig(output_path)
plt.show()
