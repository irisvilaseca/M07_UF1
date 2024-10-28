import numpy as np
from numpy import random
def generarMatriu():
    matriu = np.random.randint(0, 80, size=(3, 4))
    print(matriu)
    return matriu
def transposarMatriu(matriu):
    matriuRedimensionada = np.transpose(matriu)
    print(matriuRedimensionada)
    return matriuRedimensionada
def modificarMatriu(matriuTransposada):
    matriuModificada=[]
    valorARepetir = matriuTransposada[0, -1]
    matriuModificada[:, -1] = valorARepetir
    print(matriuModificada)
    return matriuModificada