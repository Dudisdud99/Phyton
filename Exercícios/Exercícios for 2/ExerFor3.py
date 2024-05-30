maior = 0
for i in range (1,11):
    num = int(input("Digite um numero inteiro: "))
    if num > maior:
        maior = num
    if i == 1:
        menor = num
    elif num < menor:
        menor = num
print(f"O maior numero digitado foi {maior}")
print(f"O menor numero digitado foi {menor}")