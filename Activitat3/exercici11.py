diccionariDivises={
    "lliura esterlina":'£',
    "dòlar dels estats units":'$',
    "euro":'€',
    "ien":'¥',
    "peso":'$'
}
print(f"Introdueix una divisa")
divisa=input().lower()

if(divisa in diccionariDivises):
    print(f"El símbol de la divisa {divisa} és {diccionariDivises[divisa]}")
else:
    print(f"La divisa no es troba al diccionari")