x = []
y = []
z = []

n = 5

for i in range (n):
    x.append(int(input(f"Digite um valor para {i+1} posicao de x: ")))

for i in range (n):
    y.append(int(input(f"Digite um valor para {i+1} posicao de y: ")))

z = x + y
    
print(z)