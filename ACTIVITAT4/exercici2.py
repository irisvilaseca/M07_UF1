import numpy as np
def crearArrayUnidimensional():
    arrayUnidimensional = np.array([88,23,39,41])
    print(arrayUnidimensional)
    return arrayUnidimensional

def crearMatriu():
    matriu=[]
    fila1=[76.4, 21.7, 38.4]
    matriu.append(fila1)
    fila2=[41.2, 52.8, 88.9]
    matriu.append(fila2)
    arrayNumpy=np.array(matriu)
    print(arrayNumpy)
    return arrayNumpy
def arrayEspecial():
    arrayOriginal=np.array([12,4,9,8])
    arrayModificat=np.reshape(arrayOriginal,(4,1))
    print(arrayModificat)
    return arrayModificat
if __name__ == '__main__':
    crearArrayUnidimensional()