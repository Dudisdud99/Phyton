import numpy as np
x = 10
y = np.zeros(x)
maiorP = 0
menorP = 0
for i in range(0, x):
    y[i] = int(input('Digite um número: '))
    if y[i] > y[maiorP]:
        maiorP = i
    if y[i] < y[menorP]:
        menorP = i
print(f'Maior valor: {y[maiorP]} na posição {maiorP}')
print(f'Menor valor: {y[menorP]} na posição {menorP}')