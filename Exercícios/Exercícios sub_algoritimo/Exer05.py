# Construa uma função que receba como parâmetro uma matriz
# quadrada 4 X 4 e retorne a soma dos valores da diagonal
# principal.

import numpy as np
np.set_printoptions(legacy='1.25')

a = np.random.randint(0,10,(4,4))

def soma_diag(a):
    return np.trace(a)

print(a,"\n")
print("soma da diagonal: ",soma_diag(a))
