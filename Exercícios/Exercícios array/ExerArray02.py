import numpy as np
x = 5
y = np.zeros(x)
soma = 0
for i in range(0, x):
    y[i] = int(input('Digite um número: '))
    soma += y[i]
print(f'Soma: {soma:.2f}')