x = input("Digite algo: ")
y = list(x)
z = []

for i in range (len(x)):
    if y[i] not in z:
        z.append(y[i])
        print(f"{y[i]}: {x.count(y[i])}")