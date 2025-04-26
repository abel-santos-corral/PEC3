import numpy as np

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mComplementarios de VarA y VarB\033[0m")

# Datos conocidos:
H_A_value = 0.2
VH_value = 0.0
H_B_value = 0.4

# Complementarios usando la familia de Yager (w=2)
N_H_A = np.sqrt(1 - H_A_value**2)
N_VH = np.sqrt(1 - VH_value**2)
N_H_B = np.sqrt(1 - H_B_value**2)

# Mostrar resultados
print(f"\n\033[34mComplementarios para VarA\033[0m")
print(f"N(VH) = {N_VH}")
print(f"N(H) = {N_H_A}")

print(f"\n\033[34mComplementarios para VarB\033[0m")
print(f"N(VH) = {N_VH}")
print(f"N(H) = {N_H_B}")

# Imprimir feedback por pantalla:
print("\033[34mFinalizado...\033[0m \033[33mComplementarios de VarA y VarB\033[0m")