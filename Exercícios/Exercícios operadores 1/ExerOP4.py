saldo  = int (input('Digite o valor do depósito: '))

cheque = int (input ('\nDigite o valor que deseja para o 1 cheque: '))
saldo = saldo-(saldo*0.0038)-cheque
print(f'1 cheque = R${cheque}, saldo restante = R${saldo:.2f}')

cheque = int (input ('\nDigite o valor que deseja para o 2 cheque: '))
saldo = saldo-(saldo*0.0038)-cheque
print(f'2 cheque = R${cheque}, saldo restante = R${saldo:.2f}')

