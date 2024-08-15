x = input("Digite algo 1: ")
y = input("Digite algo 2: ")

if x.find(y) != -1:
    print(f"Achou {y} no {x}")
else:
    print(f"n achou {y} no {x}")