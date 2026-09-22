#CLASSE PAI

class Animal:
    def __init__(self, tipo, idade, regiao):
        self._tipo = tipo
        self.__idade = idade
        self._regiao = regiao



    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def regiao(self):
        return self._regiao


    def comer(self):
        print(f"O animal {self._tipo} está comendo.")

    def dormir(self):
        print(f"O animal {self._tipo} está dormindo...")

    def mostraIdade(self):
        print(f"O animal {self._tipo} tem {self.__idade} anos de idade.")

