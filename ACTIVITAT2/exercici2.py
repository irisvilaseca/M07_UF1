def funcio2():
    ivaCorrecte=false
    IVAvalids=[4,10,21]
    preuFinal=0
    print("Introdueix un import")
    import=int(input())
    while(!ivaCorrecte){
        print("Introdueix un IVA")
        IVA=input();
        ivaCorrecte= IVA in IVAvalids
    }
    preuFinal=import*(IVA/100)
    print("L'import indicat és {import} , el valor de l'IVA és {IVA} i el preu final és {import}")
