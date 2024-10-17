x=int(input("Digite um número: "))
y=int(input("Digite um número: "))

def maior(x,y):
    if x>y:
        return x
    else:
        return y
    
print(f"o maior é: {maior(x,y)}")