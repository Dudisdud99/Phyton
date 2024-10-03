import numpy as np

matriz = np.zeros((5, 5))

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Digite o valor da linha {i+1} e coluna {j+1}: "))
        
print(matriz)
        