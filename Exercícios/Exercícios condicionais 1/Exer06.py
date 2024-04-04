dia = int(input('Digite um dia: '))
mes = int(input('Digite um mes: '))
ano = int(input('Digite um ano: '))
add_dias = int(input('Digite quantos dias desaja dicionar: '))

dias = ano*365 + mes*30 + dia + add_dias
ano = dias // 365
mes = (dias - 365 * ano) // 30
dia = dias - 365 * ano - 30 * mes

if dia == 0:
    dia = 30
    mes = mes-1    

print(f'A nova data é {dia:.0f}/{mes:.0f}/{ano:.0f}')