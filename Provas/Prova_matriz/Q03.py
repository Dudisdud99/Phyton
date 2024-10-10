import numpy as np
np.set_printoptions(legacy='1.25')

x = np.zeros(100)
somaImp = 0
quantImp = 0
quantPar = 0

for i in range (len(x)):
    x[i] = int(input(f"Digite um valor: "))
    
    if x[i]%2 == 0:
        quantPar += 1
    else:
        quantImp += 1
        somaImp += x[i]

print(f"quantidade par: {quantPar}\nmedia impar: {somaImp/quantImp}")