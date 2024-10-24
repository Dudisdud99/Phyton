# Faça uma sub-rotina que recebe duas listas A e B com dez
# elementos inteiros como parâmetro. A sub-rotina deverá determinar
# e mostrar o vetor C que contém os elementos que estão em A, mas
# que não estão em B. A lista C deverá ser mostrada no programa
# principal.
import numpy as np
np.set_printoptions(legacy='1.25')

a = set(np.random.choice(range(0, 20), 10, replace=False))
b = set(np.random.choice(range(0, 20), 10, replace=False))

print("A: ",a)
print("B: ",b,"\n")

def compare(a,b):
    c = a - b
    return c

print(compare(a,b))