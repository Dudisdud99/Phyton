x=int(input("Digite um número: "))

def epar(x):
    if x%2==0:
        return True
    else:
        return False
    
print(f"{x} eh par? res: {epar(x)}")