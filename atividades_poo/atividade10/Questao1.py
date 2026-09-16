# Crie uma classe que tenha no mínimo 5 atributos, 1 construtor e 3 métodos convencionais.
# Sua classe deve ser uma das opções abaixo:
#Carro / Banco / Pessoa

#Você escolhe quais atributos relacionar com o conceito da sua classe.
#No final, quero 5 objetos diferentes instanciados, e seu programa deve exibir em uma lista FORA da classe todos os seus objetos.

class Pessoa:

    def __init__(self, nome, idade, peso, altura, profissao):
        self.nome = nome
        self.idade = idade
        self.peso = peso


    def nome_aluno(self):
        print(self.nome)

    def idade_aluno(self):
        print(self.idade)

    def peso_aluno(self):
        print(self.peso)




