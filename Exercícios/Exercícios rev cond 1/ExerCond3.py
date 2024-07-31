p1 = int(input('Digite preço: '))
p2 = int(input('Digite preço: '))
p3 = int(input('Digite preço: '))

menor = p1
if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3

print(f'O menor preço é R${menor:.2f}')