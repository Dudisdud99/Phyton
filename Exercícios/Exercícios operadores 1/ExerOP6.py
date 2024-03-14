p = int (input('Digite a quantia de pães vendidos: '))
b = int (input('Digite a quantia de broas vendidas: '))

p = 0.5*p
b = 1.5*b

print(f'\nO valor arrecadado é de R${(p+b):.2f} e o valor que deve ir para a poupança é de R${((p+b)*0.1):.2f}')
