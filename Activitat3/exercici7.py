diccionariEdats={}

while True:
    print("Introdueix un nom. Si vols sortir posa \"ny ")
    nom=input()
    if(nom in diccionariEdats):
        print("Ja existeix algú amb aquest nom")
    else:
        print("Introdueix l'edat")
        edat=int(input())
        diccionariEdats[nom]=edat
    print(f"La persona {nom} ha estat afegida amb èxit")
    
    print("Vols afegir al diccionari? S/N")
    resposta=input()
    if(resposta.upper()=="N"):
        break
print(f"Contactes finals:")
for nom,edat in diccionariEdats.items:
    print(f"{nom} {edat} anys")
