idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo (M ou F): ')

if sexo == 'F':
    if idade > 24:
        print(f'Vc é uma mulher')
    elif idade > 12 and idade < 24:
        print(f'Vc é uma moça')
    elif idade > 0 and idade <=12:
        print(f'Vc é uma menina')

else:
    if idade > 24:
        print(f'Vc é um homem')
    elif idade > 12 and idade < 24:
        print(f'Vc é um moço')
    elif idade > 0 and idade <=12:
        print(f'Vc é um menino')