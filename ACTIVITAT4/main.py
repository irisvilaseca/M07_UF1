import numpy as np
import exercici1 as ex1
import exercici2 as ex2
import exercici3 as ex3
import exercici4_irisVilaseca as ex4
from ACTIVITAT4.exercici1 import crearNdArray
from ACTIVITAT4.exercici2 import arrayEspecial
from ACTIVITAT4.exercici3 import numeroMaxim, numeroMinim
from ACTIVITAT4.exercici4_irisVilaseca import exercici4

if __name__ == '__main__':
    # EXERCICI1
    matriu = ex1.crearNdArray()
    # Imprimir la matriu de l'exercici1
    print("La matriu és: ", {matriu})

    # Imprimir la dimensió de la matriu de l'exercici1
    print(f"La dimensió de la matriu és: ", {np.ndim(matriu)})

    # Imprimir la dimensió de la matriu
    print(f"La dimensió de la matriu és: {np.ndim(matriu)}")

    # Imprimir el tamany de la matriu
    print(f"El tamany de la matriu és: {np.shape(matriu)}")

    # Imprimir el número d'elements de la matriu
    print(f"El número d'elements de la matriu és: {np.size(matriu)}")

    # Imprimir el tipus d'elements que conté la matriu
    print(f"El tipus d'elements de la matriu és: {matriu.dtype}")


    #EXERCICI2
    def mostrarDetallsMatriu(matriu, nom):
        print(f"Matriu '{matriu}':")
        print(f"\nDetalls de la matriu '{nom}':")
        print(f"Número total d'elements: {matriu.size}")
        print(f"Dimensió de la matriu: {matriu.ndim}")
        print(f"Tipus d'elements interns: {matriu.dtype}")
        print(f"Tamany de la matriu: {matriu.shape}")


    matriuUnidimensional = ex2.crearArrayUnidimensional()
    mostrarDetallsMatriu(matriuUnidimensional, "Unidimensional")
    matriu2 = ex2.crearMatriu()
    mostrarDetallsMatriu(matriu2, "Matriu bidimensional")
    arrayVertical = ex2.arrayEspecial()
    mostrarDetallsMatriu(arrayVertical, "Vertical")

    #EXERCICI3
    matriuEx3=ex3.generarMatriu()
    mostrarDetallsMatriu(matriuEx3, "Matriu Ex3")
    print(f"El valor màxim de la matriu és: {numeroMaxim(matriuEx3)}")
    print(f"El valor màxim de la matriu és: {numeroMinim(matriuEx3)}")

    #EXERCICI4
    matriuEx4=ex4.generarMatriu()
    print(f"La matriu original és '{matriuEx4}':")
    ex4.transposarMatriu(matriuEx4)
    print(f"La matriu original es transposa (gira columnes i files) i els valors que hi havia a la darrera columna es traslladen a la darrera fila '{matriu}':")
    print(f"Trobem el valor de la darrera columna a la primera fila")
    print(f"Omplim la darrera columna amb el valor repetit que hem trobat")
    ex4.modificarMatriu(matriuEx4)
