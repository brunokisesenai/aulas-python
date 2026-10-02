def cadastrar_aluno():
    aluno = input("Digite o nome do aluno: ")
    turma = input("Digite o numero da turma: ")
    nota1 = input(float("Digite a primeira nota: "))
    nota2 = input(float("Digite a segunda nota: "))
    nota3 = input(float("Digite a terceira nota: "))
    nota4 = input(float("Digite a quarta nota: "))
    media = float((nota1 + nota2 + nota3 + nota4) / 4)
    if media >= 7:
        status = "APROVADO"
    else:
        status = "REPROVADO"

#    with open("basededados.txt", "a", encoding="utf-8") as arquivo:
#        arquivo.write(f"{aluno}; {turma}; {nota1:.2f}; {nota2:.2f}; {nota3:.2f}; {nota4:.2f}; {media:.2f}; {status}\n")


    print("Aluno(a) cadastrado(a)!")

cadastrar_aluno()


def calcular_media():
    with open("basededados.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip().split(";")
            aluno = linha[0]
            media = ((linha[2] + linha[3] + linha[4] + linha[5]) / 4)
            if media >= 7:
                status = "APROVADO"
            else:
                status = "REPROVADO"
    print(f"O(a) aluno(a) {aluno} foi {status}!")






