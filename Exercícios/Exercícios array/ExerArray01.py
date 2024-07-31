import numpy as np
x = 10
y = np.zeros(x)
for i in range(0, 10):
    y[i] = int(input('Digite um número: '))
print(y)