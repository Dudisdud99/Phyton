# 1. Vamos modelar uma família com Pai, Mãe, Filhos;
# 2. Todos devem herdar da classe Pessoa;
# 3. Na classe Pai e Mãe, crie um método que irá adicionar objetos
# da classe Filhos;
# 4. Na classe Filho, crie um método que irá adicionar objetos Pai e
# Mãe;
# 5. Crie um método Resumo genérico na classe Pessoa que listará
# atributos do objeto;
# 6. Crie um método Resumo especializado para cada Classe: Pai,
# Mãe e Filhos. 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def resumo(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        
class Pai(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []
        self.esposa = None
        
    def adicionaEsposa(self, esposa):
        self.esposa = esposa
        
    def adicionaFilho(self, filho):
        self.filhos.append(filho)
        for filho in self.filhos:
            filho.adicionaPai(self)
        
    def resumo(self):
        super().resumo()
        print('Filhos:', self.filhos)
        
class Mae(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []
        self.marido = None
        
    def adicionaMarido(self, marido):
        self.marido = marido
        
    def adicionaFilho(self, filho):
        self.filhos.append(filho)
        for filho in self.filhos:
            filho.adicionaMae(self)
        
    def resumo(self):
        super().resumo()
        print('Filhos:', self.filhos)
        
class Filho(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.pai = None
        self.mae = None
        
    def adicionaPai(self, pai):
        self.pai = pai
        
    def adicionaMae(self, mae):
        self.mae = mae
        
    def resumo(self):
        super().resumo()
        print('Pai:', self.pai)
        print('Mãe:', self.mae)
        
pai = Pai('João', 40)
mae = Mae('Maria', 35)
filho = Filho('Pedro', 10)

pai.adicionaEsposa(mae)
mae.adicionaMarido(pai)

pai.adicionaFilho(filho)
mae.adicionaFilho(filho)  

pai.resumo()
mae.resumo()
filho.resumo