#CLASSE FILHA

from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome = nome, idade = idade, nivel_fome = nivel_fome)
        self._velocidade_kmh = velocidade_kmh


    def correr(self):
        print(f"O nível inicial da fome é {self.nivel_fome}.")
        self.nivel_fome += 20
        print(f"O {self.nome} correu {self._velocidade_kmh} kmh. O nível da fome subiu para {self.nivel_fome} pontos!")

    def emitir_som(self):
        print(f"O {self.nome} ruge alto!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"A velocidade do {self.nome} é {self._velocidade_kmh} kmh.")


