dia = int(input("Digite um dia: "))
mes = int(input("Digite um mes: "))
ano = int(input("Digite um ano: "))

if ano>0 or mes>0 or dia>0:
    if mes==2:
        if ano%4==0:
            if dia<=29:
                aux=1
        else:
            if dia<=28:
                aux=1
    elif mes==1 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if dia<=31:
            aux=1
    else:
        if dia<=30:
            aux=1

if aux==1:
    print("Data válida")
