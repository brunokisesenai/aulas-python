#LISTA CONJUNTA

#   index    0        1         2
alunos = ["Joao", "Fulano", "Ciclano"]
#  index  0  1  2
notas = [10, 6, 8]
#  index  0    1   2
faltas = [15, 20, 30]

turma_python = [
    alunos,  #0
    notas,   #1
    faltas   #2
]
# Exemplo 1
#for turma in turma_python:
#    print(turma)

# Exemplo 2
for turma in turma_python:
    if turma[0] in alunos:
        print(turma) #mostra a lista dos alunos
        print(turma[0]) #mostra o aluno0
        print(turma[1]) #mostra o aluno1
        print(turma[2]) #mostra o aluno2