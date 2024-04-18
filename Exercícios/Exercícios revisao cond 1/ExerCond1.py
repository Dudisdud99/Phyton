n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma nota: '))
n3 = float(input('Digite uma nota: '))

media = (n1*3 + n2*2 + n3*5)/10

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')