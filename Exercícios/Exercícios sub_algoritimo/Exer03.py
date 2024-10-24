# Crie uma sub-rotina que receba como parâmetro um vetor V[15] de
# números inteiros e substitua todos os valores negativos de A por 0. O
# vetor deverá ser mostrado no programa principal.
import numpy as np
np.set_printoptions(legacy='1.25')

v = np.random.randint(-10,10,15)

def replace(v):
    for i in range(len(v)):
        if v[i] < 0:
            v[i] = 0
    return v

print(v,"\n")
print("sem negativos: ",replace(v))