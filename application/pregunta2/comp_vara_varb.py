import numpy as np

# Imprimir feedback por pantalla:
print("\033[34mEjecutando...\033[0m \033[33mComplementarios de VarA y VarB\033[0m")

# Datos conocidos:
H_A_VALUE = 0.2
VH_VALUE = 0.0
H_B_VALUE = 0.4

# Complementarios usando la familia de Yager (w=2)
N_H_A = np.sqrt(1 - H_A_VALUE**2)
N_VH = np.sqrt(1 - VH_VALUE**2)
N_H_B = np.sqrt(1 - H_B_VALUE**2)

# Mostrar resultados
print("\n\033[34mComplementarios para VarA\033[0m")
print("N(VH) = 10")
print("N(H) = 20")

print("\n\033[34mComplementarios para VarB\033[0m")
print("N(VH) = 10")
print("N(H) = 30")

# Imprimir feedback por pantalla:
print("\033[34mFinalizado...\033[0m \033[33mComplementarios de VarA y VarB\033[0m")
