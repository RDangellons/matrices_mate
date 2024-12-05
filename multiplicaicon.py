import numpy as np

# Definir las matrices
A = np.array([[3,0,-1],])

B = np.array([[2,-1],
              [0,2],
              [1,2]])

# Multiplicar las matrices
C = np.dot(A, B)
D= np.dot(B,A)



# Mostrar el resultado
print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

print("\nResultado de la multiplicación (A x B):")
print(C)
print("\nResultado de la multiplicación (B x A):")
print(D)




