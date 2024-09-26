def funcio9():
    print("Escriu una primera paraula")
    paraula1=input()
    print("Escriu una segona paraula")
    paraula2=input()
    llarg1=len(paraula1)
    llarg2=len(paraula2)
    if(llarg1<2 or llarg2<2):
        print("Les paraules són massa curtes")
    else:
        paraula_nova1=paraula2[:2]+paraula1[2:]
        paraula_nova2=paraula1[:2]+paraula1[2:]
    print({paraula_nova1+" "+paraula_nova2})
