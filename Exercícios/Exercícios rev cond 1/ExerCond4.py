data = int(input('Digite o ano em que vc nasceu: '))
ano = int(input('Digite o ano atual: '))

idade = ano - data 

if idade >= 16:
    print(f'Vc tem {idade} anos. Pode votar')
else:
    print('Não pode votar')