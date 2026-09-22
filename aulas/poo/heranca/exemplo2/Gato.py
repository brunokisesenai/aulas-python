# CLASSE FILHA
from Animal import Animal


class Gato(Animal):
    def __init__(self, idade, nome, regiao):
        super().__init__(idade = idade, tipo = "Gato", regiao = regiao)
        self.nome = nome

    def cospePelo(self):
        print(f"O gato {self.nome} cospiu pelo...")


    def mostraIdadeDoGato(self):
        print(self._tipo)


