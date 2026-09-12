#Crie uma única função que receba como parâmetro o nome de um aluno, sua nota do primeiro, segundo, terceiro e quarto bimestre.
#Sua função deve calcular a média final desse aluno, e imprimir na tela todos os valores e informar se o aluno foi reporvado ou aprovado pela media final.
# O valor da média = 7

def aprovacao():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota do aluno no 1º bimestre: "))
    nota2 = float(input("Digite a nota do aluno no 2º bimestre: "))
    nota3 = float(input("Digite a nota do aluno no 3º bimestre: "))
    nota4 = float(input("Digite a nota do aluno no 4º bimestre: "))
    media = float((nota1 + nota2 + nota3 + nota4) / 4)
    if media >= 7:
        resultado = "aprovado(a)!"
    else:
        resultado = "reprovado(a)!"
    print(f"O(a) aluno(a) {nome} foi {resultado} com média final {media:.2f}.")

aprovacao()