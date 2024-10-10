import numpy as np
np.set_printoptions(legacy='1.25')

n = 6
x = np.zeros((n, n))
y = np.zeros((n, n))
cont = 1

# preencher x e copiar

for i in range (n):
    for ii in range (n):
        x[i][ii] = cont
        cont += 1
        y[i][ii] = x[i][ii]
        
print(f"x original:\n{x}\n")
    
# mudar linhas x
            
for i in range (n):
    for ii in range (n):
        if i == 1:
            x[4][ii] = x[i][ii]
        if i == 4:
            x[1][ii] = y[i][ii]
            
# colar x em y
            
for i in range (n):
    for ii in range (n):
        y[i][ii] = x[i][ii]
            
# trocar colunas

for i in range (n):
    for ii in range (n):
        if ii == 3:
            x[i][5] = x[i][ii]
        if ii == 5:
            x[i][3] = y[i][ii]
        
print(f"\nx mudado:\n{x}")