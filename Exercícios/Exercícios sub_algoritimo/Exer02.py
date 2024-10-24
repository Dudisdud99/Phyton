# .Faça uma sub-rotina que receba como parâmetro uma matriz(lista
# de lista) A[5][5] e retorne a soma de todos os seus elementos.
import numpy as np
np.set_printoptions(legacy='1.25')

a = np.random.randint(0,10,(5,5))

def soma(a):
    return a.sum()

print(a,"\n")

print("soma: ",soma(a))