lista_nomes = []

while True:
    novo_nome = input("Digite um nome ('fim' finliza o código): \n")

    if novo_nome == 'fim':
         break

    lista_nomes.append(novo_nome)

for nome in lista_nomes:
    print(nome)

with open("Lista_de_nomes.txt", 'w', encoding="utf-8") as arquivo:         #sobreescreve
    arquivo.write(str(lista_nomes))

#with open("Lista_de_nomes.txt", 'r', encoding="utf-8") as arquivo:
#   texto = arquivo.read()                     #lê todos os caracteres do meu arquivo
#   print(texto)


with open("Lista_de_nomes.txt", 'a', encoding="utf-8") as arquivo:          #adiciona "a de append"
    arquivo.write("Orlando")





