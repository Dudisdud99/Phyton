import numpy as np

matriz = np.zeros((5, 5))
somaLinha = 0
somaDiagonal = 0
        
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Digite o valor da linha {i+1} e coluna {j+1}: "))
        if i == 1:
            somaLinha += matriz[i][j]
        if i == j:
            somaDiagonal += matriz[i][j]
        
print(f"\n{matriz}\n\nSoma da linha 1: {somaLinha}\n\nSoma da diagonal: {somaDiagonal}")