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

    with open("basededados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{aluno}; {turma}; {nota1:.2f}; {nota2:.2f}; {nota3:.2f}; {nota4:.2f}; {status}\n")


    print(f"A média final do(a) {aluno} foi {media}. O(a) aluno(a) foi {status}!")
    print(f"Aluno(a) cadastrado(a)!")

cadastrar_aluno()



def lista_nomes_alunos():
    with open("basededados.txt", "r", encoding="utf-8") as arquivo:
        lista_alunos = arquivo.readlines()
        for aluno in lista_alunos:
            aluno  = aluno.strip().split(";")
            lista_alunos = aluno[0]

            print(f"{aluno[0]}\n")



def calcular_media():
    with open("basededados.txt", "r", encoding="utf-8") as arquivo:
        nome_busca = input("Digite o nome do aluno: ")
        lista_alunos = arquivo.readlines()
        for aluno in lista_alunos:
            aluno = aluno.strip().split(";")
            aluno[3] = float(aluno[3])
            aluno[4] = float(aluno[4])
            aluno[5] = float(aluno[5])
            aluno[2] = float(aluno[2])
            media = ((aluno[3] + aluno[4] + aluno[5] + aluno[2]) / 4 )
            if nome_busca == aluno[0]:
                print(f'A média do(a) aluno(a) {aluno[0]} foi: {media}')
            else:
                print(f'Aluno não encontrado!')




def procurar_status():
    with open("basededados.txt", "r", encoding="utf-8") as arquivo:
        nome_busca = input("Digite o nome do aluno: ")
        lista_alunos = arquivo.readlines()
        for aluno in lista_alunos:
            aluno = aluno.strip().split(";")
            aluno[3] = float(aluno[3])
            aluno[4] = float(aluno[4])
            aluno[5] = float(aluno[5])
            aluno[2] = float(aluno[2])
            media = ((aluno[3] + aluno[4] + aluno[5] + aluno[2]) / 4)
            if media >= 7:
                status = "APROVADO"
            else:
                status = "REPROVADO"
            if nome_busca == aluno[0]:
                print(f'O status do(a) aluno(a) {aluno[0]} é: {status}!')
            else:
                print(f'Aluno não encontrado!')



def mostrar_maior_media():
    with open("basededados.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        lista_media = []

        for linha in linhas:
            linha = linha.strip().split(";")
            lista_media.append(float(linha[6]))

        maior_media = max(lista_media)

        print(f"A maior média foi: {maior_media}")



def mostrar_menor_media():
    with open("basededados.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        lista_media = []

        for linha in linhas:
            linha = linha.strip().split(";")
            lista_media.append(float(linha[6]))

        menor_media = min(lista_media)

        print(f"A menor média foi: {menor_media}")



#SIMULANDO UM SISTEMA FUNCIONAL

while True:
    finalizar = False
    print("\n\n\n==========SISTEMA DE NOTAS==========\n\n")
    opcao = int(input("Escolha uma das opções:\n"
                  "1) Cadastrar novo aluno\n"
                  "2) Calcular média\n"
                  "3) Procurar status de aprovação\n"    
                  "4) Maior média\n"
                  "5) Menor média\n"
                  "6) Listar alunos\n"
                  "7) Finalizar programa\n"))

    match opcao:
        case 1:
            cadastrar_aluno()
        case 2:
            calcular_media()
        case 3:
            procurar_status()
        case 4:
            print(mostrar_maior_media())
        case 5:
            print(mostrar_menor_media())
        case 6:
            lista_nomes_alunos()
        case _:
            print("Finalizando programa...")
            finalizar = True
            break