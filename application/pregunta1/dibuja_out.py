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

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mGráfico de Out\033[0m")

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

# Función para anotar pendiente (ahora recibe texto directamente)
def annotate_slope(label_pos, slope_text, rotation=0):
    plt.annotate(slope_text, xy=label_pos, textcoords="offset points",
                 xytext=(0, 10), ha='center', fontsize=12, color='black', rotation=rotation)

# Anotar pendiente de VL
annotate_slope((13, 0.6), "1-0,025x", rotation=-55)  # posición del texto + pendiente manual
# Anotar pendiente de L
annotate_slope((26, 0.6), "0,025x", rotation=56)
annotate_slope((48, 0.6), "2,333-0,0333x", rotation=-60)
# Anotar pendiente de M
annotate_slope((61, 0.6), "0,0333x-1,333", rotation=60)
annotate_slope((77, 0.6), "4,5-0,05x", rotation=-72)
# Anotar pendiente de H
annotate_slope((84, 0.65), "0,05x-3,5", rotation=68)
annotate_slope((93.9, 0.65), "10-0,1x", rotation=-78)
# Anotar pendiente de VH
annotate_slope((99.5, 0.65), "0,1x-9", rotation=74)

plt.title('Funciones de Membresía de Out')
plt.xlabel('Out')
plt.ylabel('Grado de pertenencia')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()

# Ajustar el layout para incluir la leyenda
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Crear directorio y guardar imagen
output_dir = 'data/respuesta1'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'Out.png'))
plt.show()

# Imprimir feedback por pantalla:
print("\033[34mFinalizado...\033[0m \033[33mGráfico de Out\033[0m")
