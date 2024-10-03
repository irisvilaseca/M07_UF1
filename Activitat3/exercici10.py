abecedari = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedariSenseMultiples=[]

for i in range(len(abecedari)):
    if ((i+1)%3!=0):
        abecedariSenseMultiples.append(abecedari[i])

abecedariTupla=tuple(abecedariSenseMultiples)

for lletra in abecedariSenseMultiples:
    print(lletra)

for lletra in abecedariTupla:
    print(lletra)