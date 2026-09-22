#CLASSE PAI

class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = nivel_fome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade >=0:
            self.__idade = idade
            print(f"A idade é: {self.__idade}!")
        else:
            print(f"Erro! Idade Inválida!")

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, nivel_fome):
        if (nivel_fome > 0) and (nivel_fome < 100):
            self.__nivel_fome = nivel_fome
            print(f"O nível da fome é: {self.__nivel_fome}!")
        else:
            if nivel_fome < 0:
                self.__nivel_fome = 0

            else:
                self.__nivel_fome = 100
            print(f"O nível da fome é: {self.__nivel_fome}!")

    def alimentar(self, porcao):
        if porcao > 0:
            if self.__nivel_fome >= porcao:
                self.__nivel_fome -= porcao
                print(f"O {self.nome} foi alimentado e o nível da fome diminuiu para: {self.__nivel_fome}!")
        else:
            print(f"Erro: Porção inválida!")

    def emitir_som(self):
        print(f"O {self.__nome} faz um som genérico!")

    def exibir_resumo(self):
        print(f"O {self.__nome} possui {self.__idade} anos e nível de fome {self.__nivel_fome}.")