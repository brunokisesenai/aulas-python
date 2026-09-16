# Crie uma classe que tenha no mínimo 5 atributos, 1 construtor e 3 métodos convencionais.
# Sua classe deve ser uma das opções abaixo:
#Carro / Banco / Pessoa

#Você escolhe quais atributos relacionar com o conceito da sua classe.
#No final, quero 5 objetos diferentes instanciados, e seu programa deve exibir em uma lista FORA da classe todos os seus objetos.

class Pessoa:

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso


    def nome_aluno(self):
        print(self.nome)

    def idade_aluno(self):
        print(self.idade)

    def peso_aluno(self):
        print(self.peso)


pessoa1 = Pessoa(nome = "Bruno", idade = 44, peso = 90)
pessoa2 = Pessoa(nome = "Carlos", idade = 30, peso = 64)
pessoa3 = Pessoa(nome = "Daniel", idade = 25, peso = 72)
pessoa4 = Pessoa(nome = "Eduardo", idade = 16, peso = 81)
pessoa5 = Pessoa(nome = "Fernando", idade = 60, peso = 59)

print(pessoa1.nome_aluno(), pessoa1.idade_aluno(), pessoa1.peso_aluno())
print(pessoa2.nome_aluno(), pessoa2.idade_aluno(), pessoa2.peso_aluno())
print(pessoa3.nome_aluno(), pessoa3.idade_aluno(), pessoa3.peso_aluno())

