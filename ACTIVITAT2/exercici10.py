import random
def funcio10():
    num_aleatori=random.randint(1,100)
    encertat=False
    intents=0
    while encertat==False:
            print("Introdueix el número que creus que és")
            try:
                endevinat=int(input())
                intents+=1
                if endevinat==num_aleatori:
                    encertat=True
                elif num_aleatori>endevinat:
                        print("El número pensat és més gran")
                else:
                        print("El número pensat és més petit")
            except ValueError:
                print("Has introduït un valor no numèric o fora de rang")
    print("El número pensat era {num_aleatori} i l'has encertat en {intents} intents")