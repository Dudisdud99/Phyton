num = int(input("Digite um numero inteiro: "))
aux=num
print(f"{num}! = ")
for i in range(1,num):
    print(f"{i}.")
    num *= i
print(f"{aux}\n= {num}")    