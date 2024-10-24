# Crie uma função chamada calculadora que recebe dois números e
# uma operação (adição, subtração, multiplicação ou divisão). A função
# deve retornar o resultado da operação ou uma mensagem de erro
# caso a operação seja inválida.

import numpy as np
np.set_printoptions(legacy='1.25')

def calculadora(x,y,op):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "*":
        return x*y
    elif op == "/":
        return x/y
    else:
        return "operação inválida"

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
op = input("'+' para adição, '-' para subtração, '*' para multiplicação e '/' para divisão: ")

print("resposta: ",calculadora(x,y,op))
