
class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
    def descricao(self):
        return f"Cor: {self.cor}, ano: {self.ano}"


carro1 = Carro("vermelho", "2020")

