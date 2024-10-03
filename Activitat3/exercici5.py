print("Intodueix una frase")
frase = input()
frase_desespaiada=tuple(frase.replace(" ",""))
frase_sense_duplicats=""
for lletra in frase_desespaiada:
    if(lletra not in frase_sense_duplicats):
        frase_sense_duplicats+=lletra
print("El contingut de la tupla és: {frase_desespaiada} i les lletres sense duplicats són {frase_sense_duplicats}")