import numpy as np
x = 5
maior = 0
menor = 0
y = np.zeros(x)
for i in range(1, x):
    y[i] = int(input('Digite um número: '))
    if i == 0:
        maior = y[i]
        menor = y[i]
    else:
        if y[i] > maior:
            maior = y[i]
        if y[i] < menor:
            menor = y[i]
print(f'Maior: {maior}')
print(f'Menor: {menor}')