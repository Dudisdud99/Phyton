import numpy as np
x = 5
y = np.zeros(x)
media = 0
for i in range(0, x):
    y[i] = int(input('Digite um número: '))
    media += y[i]
media /= x
print(f'Média: {media:.2f}')