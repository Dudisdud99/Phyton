# Implementar os métodos abaixo para a classe Carro:
# a. ligarMotor
# b. desligarMotor
# c. andar
# d. parar
# 2. Criar atributos para:
# a. Status do motor (ligado/desligado)
# b. Status do movimento do carro (andando/parado)
# 3. Criar métodos para informar (exibir na tela) o status acima.

class Carro:
    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 2010
    kmRodados = 0

    def detalhes(self):
        print('cor:', self.cor)
        print('marca:', self.marca)
        print('modelo:', self.modelo)
        print('ano:', self.ano)
        print('km rodados:', self.kmRodados)
        passageiro = True
        print('passageiro:', passageiro)

    def adicionaKmRodados(self, km):
        self.kmRodados += km
        
    def ligarMotor(self):
        print('Motor ligado')
        
    def desligarMotor(self):
        print('Motor desligado')
        
    def andar(self):
        print('Carro andando')
        
    def parar(self):
        print('Carro parado')
        
    def statusMotor(self):
        print('Motor ligado')
        
    def statusMovimento(self):
        print('Carro andando')
        
carro = Carro()

carro.cor = 'preto'
carro.marca = 'Fiat'
carro.modelo = 'Uno'
carro.ano = 2010
carro.kmRodados = 50000

carro.adicionaKmRodados(100)

carro.detalhes()