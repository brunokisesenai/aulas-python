#Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)
#Construa um sistema escolar que leia a Nota 1 e a Nota 2 de um aluno, além da sua Porcentagem de Frequência. O programa deve primeiro calcular a média das notas. Para o aluno ser aprovado, ele precisa de duas coisas ao mesmo tempo: uma média maior ou igual a 6.0 E uma frequência maior ou igual a 75. Exiba a média calculada e, em seguida, exiba True se ele foi aprovado ou False se reprovou, usando o operador and.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
horas = float(input("Digite a quantidade de horas de aula assistidas: "))
frequencia = int((100 * horas) / 200)
print("A frequência do aluno foi de:", frequencia, "%")

aprovado = media >= 6.0 and frequencia >= 75
print("O aluno foi aprovado: ", aprovado)