import numpy as np

matriz = np.zeros((5, 5))

for i in range(5):
    for j in range(5):
        matriz[j][i] = int(input(f"Digite o valor da linha {j+1} e coluna {i+1}: "))
        
print(matriz)
        