print("Dóna'm un número entre 10 i 100")
ultimNumero=int(input())
tupla=[]
for i in range (1,ultimNumero):
    tupla.append(i+1)
    print(tupla[i-1])