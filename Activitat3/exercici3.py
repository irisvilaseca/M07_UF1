print("Digues un número entre 1 i 10")
numero=int(input())
tuplaResultat=[]
for i in range (1,10):
    tuplaResultat.append(numero*i)
    print(tuplaResultat[i])