import numpy as np
np.set_printoptions(legacy='1.25')

x = np.zeros(8)
neg = []
pos = []

for i in range (len(x)):
    x[i] = int(input(f"Digite um valor: "))
    if x[i] != 0:
        if x[i] < 0:
           neg.append(x[i]) 
        else:
            pos.append(x[i])


print(f"{neg}\n{pos}")