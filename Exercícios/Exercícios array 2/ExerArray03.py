x = []
y = []
z = []

for i in range (5):
    x.append(int(input(f"Digite um valor para {i+1} posicao de x: ")))

for i in range (5):
    y.append(int(input(f"Digite um valor para {i+1} posicao de y: ")))

for i in range (5):
    z.append(x[i]+y[i])
    
print(z)