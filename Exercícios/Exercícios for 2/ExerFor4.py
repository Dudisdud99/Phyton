x = int(input("Digite o número do intervalo inferior: "))
y = int(input("Digite o número do intervalo superior: "))
z = 0
for i in range(x+1, y):
    if i%2 == 0:
        z+=i
print(f"{z}")