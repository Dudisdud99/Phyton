id = int(input('Digite o codigo do produto: '))

if id == 1:
    print('O produto esta classificado como : Alimento não-perecível')
elif id == 2 or id == 3 or id == 4:
    print('O produto esta classificado como : Alimento perecível')
elif id == 5 or id == 6:
    print('O produto esta classificado como : Vestuário')
elif id == 7:
    print('O produto esta classificado como : Higiene Pessoal')
elif id >= 8 and id <= 15:
    print('O produto esta classificado como : Limpeza e Utensílios Domésticos')
else:
    print('Código inválido')