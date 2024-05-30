soma = 0
i = 0
for ii in range(0, 20):
    x = float(input(f"Digite o {ii+1} número: "))
    if x<0:
        i+=1
    else:
        soma+=x
print(f"Você digitou {i} números negativos")
print(f"A soma total dos positivos é: {soma}")