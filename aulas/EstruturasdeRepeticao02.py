# REPETIÇÃO FOR (para)

#item (variável) objeto, função, lista
#numero_digitado = int(input("Digite um número: "))
#for numero_secreto in range (1, 11):

#    if numero_digitado == numero_secreto:
#        print("Você ganhou!")


"-------------------------------------------------------------------------"

#criando uma lista
#                      0         1         2         3
#lista_de_alunos = ["aluno1", "aluno2", "aluno3", "aluno4"]
#print(lista_de_alunos)
#print(lista_de_alunos[0]) #print da posição '0' da lista

#print(type(lista_de_alunos))
#print(type(lista_de_alunos[0]))

#for valor in lista_de_alunos:
#    print(valor)
#lista_de_alunos.append("aluno4")  ->  'append' acrescenta um item à lista


"-----------------------------------------------------------------------------"

#CRIANDO UMA TUPLA

#tupla_de_alunos = ("aluno1", "aluno2", "aluno3") #imutável

"------------------------------------------------------------------------------"
#lista_de_alunos = []
#print(lista_de_alunos)

#while True:
#    lista_de_alunos.append(input("Digite um aluno: "))
#    opcao = input("Quer adicionar outro aluno? [S/N] ")
#    if opcao == "N":
#        break
#print(lista_de_alunos)


"---------------------------------------------------------------------------------"

#turma_python = [
#    ["Bruno", 12, 5.5],   #list
#    ("João", 0 , 10.0),   #tuple
#    "Victor"              #string
#]

#print("Tipo da lista: ", type(turma_python))
#print("Tipo do primeiro valor: ", type(turma_python[0]))
#print("Tipo do segundo valor: ", type(turma_python[1]))
#print("Tipo do terceiroo valor: ", type(turma_python[2]))

#turma_python[2] = ["Victor", 15, 10.0]
#print("Tipo da lista: ", type(turma_python))
#print(list(turma_python))

"----------------------------------------------------------------------------------"

#FUNÇÕES DE LISTAS

list_numeros = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#debug mode
for numero in list_numeros:  #breakpoint
    if numero == 3:
        list_numeros.remove(3)

print(list_numeros)

