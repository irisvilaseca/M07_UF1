print("Escriu 10 números separats per un espai")
numeros=input()
numerosEnLlista=numeros.split()
sumaNumeros=0
for i in numerosEnLlista:
    sumaNumeros+=int(i)

mitja=sumaNumeros/(len(numerosEnLlista))
llistaResultats=[sumaNumeros, mitja]
numerosEnLlista.extend(llistaResultats)
print(f"Números de l'usuari: {numerosEnLlista}, Suma total: {sumaNumeros} i Mitjana: {mitja}")
