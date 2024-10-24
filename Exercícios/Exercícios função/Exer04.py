altura=int(input("Digite um número: "))
base=int(input("Digite um número: "))

def calcular_area_triangulo(altura,base):
    return (altura*base)/2

print(f"A area do triangulo é: {calcular_area_triangulo(altura,base)}")