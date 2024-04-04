x = int(input('Digite um valor para X: '))
y = int(input('Digite um valor para Y: '))

if 0.3*(x+y) > 500:
    aux = x
    x = y
    y = aux
    print(f'X = {x} e Y = {y}')
else:
    if x > y:
        print(f'O maior é {x}')
    else:
        print(f'O maior é {y}')


