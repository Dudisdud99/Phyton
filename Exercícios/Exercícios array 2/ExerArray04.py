x = []
y = []
z = []

n = 5
m = 0

for i in range (n):
    x.append(int(input(f"Digite um valor para {i+1} posicao de x: ")))

for i in range (n):
    y.append(int(input(f"Digite um valor para {i+1} posicao de y: ")))

for i in range (n):
    m = n - i -1
    z.append(y[m])
    
for i in range (n):
    y[i] = (z[i] * x[i])
    
print(y)