# activacion_out.py

import os
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import pickle

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mDiagrama Out activado y valor nítido\033[0m")

# Definir rango
x = np.linspace(0, 100, 1001)

# Definir funciones de membresía triangulares
VL = fuzz.trimf(x, [0, 0, 40])
L = fuzz.trimf(x, [0, 40, 70])
M = fuzz.trimf(x, [40, 70, 90])
H = fuzz.trimf(x, [70, 90, 100])
VH = fuzz.trimf(x, [90, 100, 100])

# Activaciones dadas
activaciones = {
    'VL': 1.0,
    'L': 1.0,
    'M': 1.0,
    'H': 1.0,
    'VH': 0.4472
}

# Recortar funciones por activación
VL_recortado = np.fmin(activaciones['VL'], VL)
L_recortado = np.fmin(activaciones['L'], L)
M_recortado = np.fmin(activaciones['M'], M)
H_recortado = np.fmin(activaciones['H'], H)
VH_recortado = np.fmin(activaciones['VH'], VH)

# Unión de todas las funciones recortadas (máximo en cada x)
union = np.fmax(VL_recortado,
         np.fmax(L_recortado,
         np.fmax(M_recortado,
         np.fmax(H_recortado, VH_recortado))))

# Calcular valor nítido (centroide)
valor_nitido = fuzz.defuzz(x, union, 'centroid')

# Graficar
plt.figure(figsize=(12, 7))

# Funciones originales
plt.plot(x, VL, 'orange', linestyle='--', linewidth=1, label='VL Original')
plt.plot(x, L, 'green', linestyle='--', linewidth=1, label='L Original')
plt.plot(x, M, 'red', linestyle='--', linewidth=1, label='M Original')
plt.plot(x, H, 'blue', linestyle='--', linewidth=1, label='H Original')
plt.plot(x, VH, 'black', linestyle='--', linewidth=1, label='VH Original')

# Funciones recortadas
plt.fill_between(x, 0, VL_recortado, facecolor='orange', alpha=0.5)
plt.fill_between(x, 0, L_recortado, facecolor='green', alpha=0.5)
plt.fill_between(x, 0, M_recortado, facecolor='red', alpha=0.5)
plt.fill_between(x, 0, H_recortado, facecolor='blue', alpha=0.5)
plt.fill_between(x, 0, VH_recortado, facecolor='black', alpha=0.5)

# Unión final
plt.plot(x, union, 'magenta', linewidth=2, label='Unión de Activaciones')

# Valor nítido
plt.axvline(valor_nitido, color='magenta', linestyle=':', linewidth=2, label=f'Valor nítido: {valor_nitido:.2f}')

# Anotar pendientes
def annotate_slope(label_pos, slope_text, rotation=0):
    plt.annotate(slope_text, xy=label_pos, textcoords="offset points",
                 xytext=(0, 10), ha='center', fontsize=12, color='black', rotation=rotation)

annotate_slope((14, 0.6), "1-0,025x", rotation=-61)
annotate_slope((25, 0.6), "0,025x", rotation=58)
annotate_slope((46, 0.6), "2,333-0,0333x", rotation=-65)
annotate_slope((60, 0.6), "0,0333x-1,333", rotation=70)
annotate_slope((77, 0.6), "4,5-0,05x", rotation=-75)
annotate_slope((84, 0.65), "0,05x-3,5", rotation=75)
annotate_slope((93.9, 0.65), "10-0,1x", rotation=-80)
annotate_slope((99.5, 0.65), "0,1x-9", rotation=75)

# Gráfica final
plt.title('Funciones de Membresía y Activaciones Recortadas de Out')
plt.xlabel('Out')
plt.ylabel('Grado de pertenencia')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Crear directorio y guardar imagen
output_dir = 'data/respuesta3'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'Out_activacion_union_nitido.png'))
plt.show()

# Imprimir resultado
print("\033[32mValor nítido calculado:\033[0m", round(valor_nitido, 2))

# Calcular Centro de Masa manualmente (sumatorio)
numerador = np.sum(union * x)
denominador = np.sum(union)
valor_nitido_sumatorio = numerador / denominador

print("\n\033[32mCálculo manual por sumatorio:\033[0m")
print(f"  Numerador (Σ µ(x)·x) = {numerador:.4f}")
print(f"  Denominador (Σ µ(x)) = {denominador:.4f}")
print(f"  CoM(x) = {valor_nitido_sumatorio:.4f}")

print("\033[34mFinalizado...\033[0m \033[33mDiagrama Out activado y valor nítido\033[0m")
