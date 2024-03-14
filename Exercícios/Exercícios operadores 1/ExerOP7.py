saldo = int (input('Digite quntos R$ de gasolina deseja colocar: '))
preco = float (input('Digite o preço da gasolina: '))

gasolina = saldo/preco

print(f'Vc encheu {gasolina:.2f} com R${saldo:.2f}')
