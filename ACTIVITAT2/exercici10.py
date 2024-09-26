import random
def funcio10():
    num_aleatori=random.randint(1,100)
    encertat=false
    intents=0
    while encertat==false:
            print("Introdueix el número que creus que és")
            endevinat=int(input())
            intents+=1
            if endevinat==num_aleatori:
                encertat=true
            else:
                if num_aleatori>endevinat:
                    print("El número pensat és més gran")
                else:
                    print("El número pensat és més petit")
    print("El número pensat era {num_aleatori} i l'has encertat en {intents} intents")