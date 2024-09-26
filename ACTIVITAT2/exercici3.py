def funcio3():
    resultat=0
    print("Introdueix un valor numèric")
    valor1=int(input())
    print("Introdueix el segon valor numèric")
    valor2=int(input())
    if(valor1>=valor2):
        resultat=valor1
    else:
        resultat=valor2
    
    print("El nombre més gran és {resultat}")
