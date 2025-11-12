
import numpy as np

# ==============================================================
#  EJEMPLO 1: CÁLCULO Y VERIFICACIÓN DE AUTOVALORES Y AUTOVECTORES
# ==============================================================

print("=============================================")
print("EJEMPLO 1: Cálculo y verificación de autovalores y autovectores")
print("=============================================\n")

# Definimos una matriz cuadrada 3x3
A = np.array([[4, 2, 1],
              [0, 3, -1],
              [0, 0, 2]])

# Calculamos autovalores y autovectores
valores, vectores = np.linalg.eig(A)

print("Matriz A:")
print(A)

print("\nAutovalores:")
print(valores)

print("\nAutovectores (columnas):")
print(vectores)

# Verificación de la ecuación A·v = λ·v
print("\nVerificación de la ecuación A·v = λ·v para cada par:")
for i in range(len(valores)):
    lambda_i = valores[i]
    v_i = vectores[:, i]
    lado_izq = np.dot(A, v_i)
    lado_der = lambda_i * v_i
    print(f"\nAutovalor λ{i+1} = {lambda_i:.4f}")
    print("A·v =", np.round(lado_izq, 4))
    print("λ·v =", np.round(lado_der, 4))

# ==============================================================
#  EJEMPLO 2: MATRIZ NO TRIANGULAR Y PROPIEDADES DE AUTOVECTORES
# ==============================================================

print("\n\n=============================================")
print("EJEMPLO 2: Matriz simétrica (autovectores ortogonales)")
print("=============================================\n")

# Matriz simétrica 3x3
B = np.array([[2, 1, 0],
              [1, 2, 1],
              [0, 1, 2]])

# Cálculo de autovalores y autovectores
valores_B, vectores_B = np.linalg.eig(B)

print("Matriz B:")
print(B)

print("\nAutovalores:")
print(np.round(valores_B, 4))

print("\nAutovectores (columnas):")
print(np.round(vectores_B, 4))

# Comprobación con el primer autovalor y autovector
lambda1 = valores_B[0]
v1 = vectores_B[:, 0]

print(f"\nComprobación para λ1 = {lambda1:.4f}")
print("B·v =", np.round(np.dot(B, v1), 4))
print("λ·v =", np.round(lambda1 * v1, 4))

print("\nNota: Al ser una matriz simétrica, los autovalores son reales y los autovectores son ortogonales entre sí.\n")

# ==============================================================
# ⚙️ EJEMPLO 3: APLICACIÓN PRÁCTICA – ANÁLISIS DE ESTABILIDAD
# ==============================================================

print("\n=============================================")
print("EJEMPLO 3: Aplicación práctica – Análisis de estabilidad")
print("=============================================\n")

# Matriz que representa un sistema dinámico lineal
A_sistema = np.array([[-2, 1, 0],
                      [0, -1, 1],
                      [0, 0, -3]])

# Cálculo de autovalores
valores_sistema, _ = np.linalg.eig(A_sistema)

print("Matriz del sistema A:")
print(A_sistema)

print("\nAutovalores del sistema:")
print(np.round(valores_sistema, 4))

# Análisis de estabilidad
if np.all(np.real(valores_sistema) < 0):
    print("\n El sistema es ESTABLE: todas las trayectorias tienden al equilibrio.")
elif np.any(np.real(valores_sistema) > 0):
    print("\n El sistema es INESTABLE: existen trayectorias que divergen.")
else:
    print("\n El sistema tiene modos oscilatorios (autovalores con parte imaginaria).")

print("\nFIN DEL PROGRAMA ")
