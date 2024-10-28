import numpy as np
from numpy import random
def generarMatriu():
    matriu=np.array(range(0,100),dtype=int)
    for i in matriu:
        matriu[i]=random.randint(101)
    print(matriu)
    files=int(input("NÚMERO DE FILES:"))
    columnes = int(input("NÚMERO DE COLUMNES:"))
    matriu_redimensionada = np.reshape(matriu,(files,columnes))
    print(matriu_redimensionada)
    print(numeroMaxim(matriu_redimensionada))
    print(numeroMinim(matriu_redimensionada))
    return matriu_redimensionada

def numeroMaxim(matriu_entrada):
    return np.max(matriu_entrada)

def numeroMinim(matriu_entrada):
    return np.min(matriu_entrada)

if __name__ == '__main__':
    generarMatriu()