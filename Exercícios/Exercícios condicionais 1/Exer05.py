L = int(input('Digite o numero de litros: '))
tipo = (input('Digite o tipo de combustivel (G ou A): '))

if tipo == 'g':
    if L <= 20:
        valor = L*(7.20*0.97)
    else:
        valor = L*(7.20*0.95)
else:
    if L <= 20:
        valor = L*(6.50*0.96)
    else:
        valor = L*(6.50*0.94)

print(f'O valor a ser pago é R$ {valor:.2f}')