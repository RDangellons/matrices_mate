import numpy as np

# Definir las matrices
A = np.array([[3,7,1],
              [4,3,2],
              [5,4,2]])

B = np.array([[6,1,4],
              [3,2,7],
              [9,8,2]])

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




