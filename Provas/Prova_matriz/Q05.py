import numpy as np
np.set_printoptions(legacy='1.25')

n = 3
z = np.zeros(n)
x = np.zeros((n, n))
y = np.zeros((n, n))
cont = 1

for i in range (n):
    for ii in range (n):
        x[i][ii] = int(input(f"Digite um valor pra matriz: "))
        
print("\n")
        
for i in range (n):
    z[i] = int(input(f"Digite um valor pro vetor: "))
    
for i in range (n):
    for ii in range (n):
        y[i][ii] = z[i] * x[ii][i]
        
print(f"\nVetor:\n{z}")   
print(f"\nMatriz:\n{x}") 
print(f"\nresultado:\n{y}")