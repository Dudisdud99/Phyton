x = []

for i in range (10):
    x.append(int(input(f"Digite um valor para {i+1} posicao: ")))
    if x[i]%2==0:
        x[i] = x[i] * i
    else:
        x[i] = i
print(x)