#QUESTÃO 1

"""Crie uma lista que armazene um número x de funcionários. Usando o while, adicione quantos funcionários quiser."""

"Com o for, você irá imprimir duas listas. Uma lista com todos os funcionários que receberão um aumento. Outra lista, com todos os funcionários que serão demitidos"

"Você irá decidir qual funcionário será demitido ou receberá um aumento pelo index do funcionário lista[]"

lista_funcionarios = []




while True:
    funcionario = input("Digite o nome do funcionário para criar a lista inicial: ")
    lista_funcionarios.append(funcionario)

    opcao = input("Deseja continuar? [S/N] ")
    if opcao == 'N':
        break

print("A lista de funcionários é: ", lista_funcionarios)

aumento = []

for i in lista_funcionarios:
    resposta = input(f"O funcionário {i} tem a aumento? [S/N] ")
    if resposta == 'S':
        aumento.append(i)

demitido = []

for i2 in lista_funcionarios:
    resposta2 = input(f"O funcionário {i2} será demitido? [S/N] ")
    if resposta2 == 'S':
        demitido.append(i2)

print(f"A lista de funcionários inicial é:\n {lista_funcionarios}")
print(f"A lista de funcionários que terão aumento é:\n {aumento}")
print(f"A lista de funcionários que serão demitidos é:\n {demitido}")


