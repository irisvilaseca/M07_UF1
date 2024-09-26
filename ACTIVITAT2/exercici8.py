def funcio8():
    print("Escriu entre 1 i 3 paraules")
    entrada=input()
    llista_paraules=entrada.split()
    llargada=len(llista_paraules)
    if(llargada<1 or llargada>3):
        print("Has posat el número de paraules incorrectes")
    
    for paraula in llista_paraules:
        print("La paraula {paraula} comença amb una {paraula[0]} i acaba en {paraula[-1]}")
