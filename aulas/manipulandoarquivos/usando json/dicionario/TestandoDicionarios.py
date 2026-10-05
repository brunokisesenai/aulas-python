lista_nomes = ['João', 'Bianca', 'Italo']
tupla_nomes = ('João', 'Bianca', 'Italo')

#if lista_nomes[2] == "Italo":
#    print("Nome encontrado")


#dicionario_nomes = {
#    "nome1": "Maria",
 #   "nome2": "Jose",
 #   "nome3": "Bruno",
#}

#print(lista_nomes)



#dicionario_ing_por = {
#    "hi": "Olá",
 #   "bye": "Tchau"
#}

#pesquisa = input ("Digita a palavra que quer traduzir:\nInglês: ")

#if pesquisa in dicionario_ing_por:
#    print(f"Português:", dicionario_ing_por[pesquisa])
#else:
#    print("Palavra não encontrada")


# class Pessoa:
#     def __init__(self, nome, idade, cpf):
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf
#
#     def identidade(self):
#         print(f"Nome da Pessoa: {self.nome}\n"
#               f"Idade: {self.idade}\n"
#               f"CPF: {self.cpf}\n")
#
# pessoa1 = {
#     "nome": "Jose",
#     "idade": 42,
#     "cpf": "111.111.111",
# }
#
# obj_pessoa = Pessoa(pessoa1["nome"],
#                     pessoa1["idade"],
#                     pessoa1["cpf"])
# obj_pessoa.identidade()



dicionario_pessoa = {
    "nome": "Fulano",
    "idade": 31,
}

print(dicionario_pessoa)

dicionario_pessoa["Cidade"] = "Brasília"
print(dicionario_pessoa.get("nome"))  #metodo get
print(dicionario_pessoa["idade"])     #
print(dicionario_pessoa.get("cpf"))  #metodo get

dicionario_pessoa.pop("idade")
print(dicionario_pessoa)

adicionar_chave = input("Digite um valor para adicionar: ")
adicionar_valor = input("Digite um valor para adicionar: ")

dicionario_pessoa[adicionar_chave] = adicionar_valor
print(dicionario_pessoa)

dicionario_pessoa["CEP"] = None
print(dicionario_pessoa)




