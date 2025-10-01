import numpy as np 

arreglo1 = np.array([1,2,3,4,5,6])

print("**** Arreglo en 1 dimension***\n")
print(arreglo1)


# Matrices. 
matriz1 = np.array([[1,2,3,4,5,6],
                   [7,8,9,10,11,12]])

print("\n**** Matriz en 2 dimensiones***\n")
print(matriz1) 


# Matrices tridimensionales.

matriz2 = np.array([[[ 1,2,3,4,5,6],
             [7,8,9,10,11,12],
             [13,14,15,16,17,18]]])

print("\n**** Matriz en 3 dimensiones***\n")
print(matriz2)
print(matriz2.shape)



