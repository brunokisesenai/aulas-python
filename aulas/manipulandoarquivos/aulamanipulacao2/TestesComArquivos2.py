class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def __str__(self):
        return f'nome: {self.nome}, idade: {self.idade}, raca: {self.raca}'


cachorro1 = Cachorro("Rex", 5, "Bulldog")
cachorro2 = Cachorro("Zeus", 4, "Pastor Alemão")
cachorro3 = Cachorro("Kika", 1, "Schnauzer")


lista = [cachorro1, cachorro2]

with open("lista_de_cachorros.txt", "w", encoding='utf-8') as arquivo:
    for cachorro in lista:
        arquivo.write(f"Cachorro: {str(cachorro)}\n")

with open("lista_de_cachorros.txt", "a", encoding='utf-8') as arquivo:
    arquivo.write(f"Cachorro: {str(cachorro3)}\n")

with open("lista_de_cachorros.txt", "r", encoding='utf-8') as arquivo:
    texto = arquivo.read()

    tamanho = len(texto)

    posicao = texto.find("Kika")

    cachorro_kika = texto[posicao:posicao+4]

print(cachorro_kika)






