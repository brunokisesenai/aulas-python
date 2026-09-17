# Crie uma classe que tenha no mínimo 5 atributos, 1 construtor e 3 métodos convencionais.
# Sua classe deve ser uma das opções abaixo:
#Carro / Banco / Pessoa


#Você escolhe quais atributos relacionar com o conceito da sua classe.
#No final, quero 5 objetos diferentes instanciados, e seu programa deve exibir em uma lista FORA da classe todos os seus objetos.

class Pessoa:

    def __init__(self, nome, idade, peso, altura, profissao, comida):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.profissao = profissao
        self.comida = comida

    def __str__(self):
        return (f"Informações da Pessoa: "
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nPeso: {self.peso}"
                f"\nAltura: {self.altura}"
                f"\nProfissão: {self.profissao}"
                f"\nComida: {self.comida}")

    def met_idade(self):
        print(f"O {self.nome} tem {self.idade} anos")

    def met_peso(self):
        print(f"O {self.nome} tem {self.peso} kg")

    def met_altura(self):
        print(f"O {self.nome} tem {self.altura} m")

    def met_profissao(self):
        print(f"A profissão do {self.nome} é: {self.profissao}")

    def met_comida(self):
        print(f"A comida preferida do {self.nome} é: {self.comida}")


pessoa1 = Pessoa("Bruno",44, 90, 1.86, "Engenheiro", "Yakissoba")
pessoa2 = Pessoa("Carlos", 30, 64, 1.70, "Professor", "Macarrão")
pessoa3 = Pessoa("Daniel",25, 72, 1.77, "Programador", "Salada")
pessoa4 = Pessoa("Eduardo", 16, 81, 1.81, "Advogado", "Sanduíche")
pessoa5 = Pessoa("Fernando", 60, 59, 1.75, "Médico", "Pizza")


dados_pessoa = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]

for pessoa in dados_pessoa:
    print(pessoa)
    pessoa.met_idade()
    pessoa.met_peso()
    pessoa.met_altura()
    pessoa.met_profissao()
    pessoa.met_comida()





