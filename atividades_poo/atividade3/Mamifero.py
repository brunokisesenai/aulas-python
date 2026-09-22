#CLASSE FILHA

from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, velocidade_kmh):
        super().__init__(nome = nome, idade = idade)
        self._velocidade_kmh = velocidade_kmh

    def correr(self):
        self.nivel_fome -= 20
        print(f"O {self.nome} correu {self.velocidade_kmh} kmh. O nível da fome subiu para {self.nivel_fome} pontos!")