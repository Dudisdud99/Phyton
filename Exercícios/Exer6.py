depi = int (input('Digite o valor do deposito: '))
taxa = int (input('Digite o percentual da taxa anual: '))
anos = int (input('Digite quantos anos: '))

val = depi

while anos>0 :

    ren = (taxa/100)*val
    anos -= 1
    val = val+ren

ren = val-depi

print(f'O rendimento foi de {ren} e o valor total é de {val}')