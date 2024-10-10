import numpy as np
np.set_printoptions(legacy='1.25')

x = np.zeros(25)
y = np.zeros(len(x))
cont = len(x) - 1

for i in range (len(x)):
    x[i] = int(input(f"Digite um valor: "))
    
for i in range (len(x)):
    y[cont] = x[i] * -1
    cont -= 1
    
print(y)