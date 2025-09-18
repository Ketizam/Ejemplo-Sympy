import sympy as sp

# ================================
# 1. Definición de símbolos
# ================================
x, y, z = sp.symbols('x y z')

# Expresión simbólica
expr = (x + y)**2 - (x**2 + 2*x*y + y**2)

print("Expresión original:", expr)
print("Simplificación:", sp.simplify(expr))   # simplifica la expresión
print("Expansión:", sp.expand((x + y + z)**3))  # expande el polinomio

# Derivada e integral
print("Derivada de sin(x)*y respecto a x:", sp.diff(sp.sin(x)*y, x))
print("Integral de exp(-x):", sp.integrate(sp.exp(-x), x))

# ================================
# 2. Operaciones con matrices
# ================================
# Definir una matriz simbólica
M = sp.Matrix([[x, y], [y, z]])
print("\nMatriz M:")
sp.pprint(M)

# Determinante
print("\nDeterminante de M:", M.det())

# Traspuesta
print("Traspuesta de M:")
sp.pprint(M.T)

# Inversa (si es invertible)
print("\nInversa de M:")
sp.pprint(M.inv())

# ================================
# 3. Evaluación numérica
# ================================
# Sustitución de valores
valores = {x: 1, y: 2, z: 3}
print("\nMatriz con valores sustituidos:")
sp.pprint(M.subs(valores))

# Determinante evaluado
print("Determinante con valores:", M.subs(valores).det())
