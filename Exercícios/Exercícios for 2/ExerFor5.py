i = 0
for ii in range(0, 15):
    x = float(input(f"Digite o {ii+1} número: "))
    if x>30:
        i+=1
print(f"Você digitou {i} números maiores que 30")