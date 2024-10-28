import numpy as np


def crearNdArray():
    arrayComptat=np.arange(0,50);
    arrayDiagonal=np.diag(arrayComptat)
    print(arrayDiagonal)
    return arrayDiagonal

if __name__ == '__main__':
    crearNdArray()