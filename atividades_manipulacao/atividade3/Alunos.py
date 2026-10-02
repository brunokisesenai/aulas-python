def cadastrar_aluno():
    aluno = input("Digite o nome do aluno: ")
    turma = input("Digite o numero da turma: ")
    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    nota3 = input("Digite a terceira nota: ")
    nota4 = input("Digite a quarta nota: ")
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    nota4 = float(nota4)
    media = float((nota1 + nota2 + nota3 + nota4) / 4)
    if media >= 7:
        status = "APROVADO"
    else:
        status = "REPROVADO"

#    with open("basededados.txt", "a", encoding="utf-8") as arquivo:
#        arquivo.write(f"{aluno}; {turma}; {nota1:.2f}; {nota2:.2f}; {nota3:.2f}; {nota4:.2f}; {media:.2f}; {status}\n")


    print("Aluno(a) cadastrado(a)!")

cadastrar_aluno()









