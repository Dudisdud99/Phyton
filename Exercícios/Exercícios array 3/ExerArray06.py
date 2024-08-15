x = input("Digite algo: ")
z = x[::-1].upper()
y = x.upper()

if z==y:
    print("e palindromo")
else:
    print("n e palindromo")