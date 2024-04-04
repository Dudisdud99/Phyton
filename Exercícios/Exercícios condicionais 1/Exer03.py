a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))
d = int(input('Digite um valor para D: '))
e = int(input('Digite um valor para E: '))

maior = a

if b > maior:
    maior = b
elif c > maior:
    maior = c
elif d > maior:
    maior = d
elif e > maior:
    maior = e
else:
    print("Inválido")

print(f'O maior é {maior}')