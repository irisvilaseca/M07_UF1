def funcio2():
    ivaCorrecte=False
    IVAvalids=[4,10,21]
    preuFinal=0
    print("Introdueix un import")
    import_total=float(input())
    while not ivaCorrecte:
        print("Introdueix un IVA")
        IVA=int(input())
        if IVA in IVAvalids:
            ivaCorrecte=True
    preuFinal=import_total*(IVA/100)
    print("L'import indicat és {import_total} , el valor de l'IVA és {IVA} i el preu final és {import}")
