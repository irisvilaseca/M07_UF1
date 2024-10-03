mesosAny=["gener", "febrer", "març", "abril", "maig", "juny", "juliol","agost", "setembre","octubre", "novembre", "desembre"]
numero=-1
while(numero!=0):
    print("Entra un número del 0 al 12");
    numero=int(input())
    if numero>=1 and numero<=12:
        print(mesosAny[numero-1])
    elif(numero==0):
        break
    else:
        print("Número fora de rang")