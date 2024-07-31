id = int(input('Digite o codigo do seu cargo: '))
sal = int(input('Digite oseu salario atual: '))

if id == 1:
    print('Escrituario')
    print(f'Seu percentual de aumento é de 50%')
    sal = sal + sal*0.5
    print(f'Seu novo salario é de R${sal:.2f}')
elif id == 2:
    print('Secretario')
    print(f'Seu percentual de aumento é de 35%')
    sal = sal + sal*0.35
    print(f'Seu novo salario é de R${sal:.2f}')
elif id == 3:
    print('Caixa')
    print(f'Seu percentual de aumento é de 20%')
    sal = sal + sal*0.2
    print(f'Seu novo salario é de R${sal:.2f}')
elif id == 4:
    print('Gerente')
    print(f'Seu percentual de aumento é de 10%')
    sal = sal + sal*0.1
    print(f'Seu novo salario é de R${sal:.2f}')
elif id == 5:
    print('Diretor')
    print(f'Seu percentual de aumento é de 0%')
    print(f'Seu novo salario é de R${sal:.2f}')