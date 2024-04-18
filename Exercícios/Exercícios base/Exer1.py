# Solicita duas variáveis do usuário
var1 = input("Digite o valor da primeira variável: ")
var2 = input("Digite o valor da segunda variável: ")

# Exibe os valores originais
print("Valores originais: ", var1, var2)

# Troca as variáveis
var1, var2 = var2, var1

# Exibe os valores após a troca
print("Valores após a troca: ", var1, var2)