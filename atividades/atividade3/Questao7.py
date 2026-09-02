#Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
idade_permitida = 16 <= idade <= 69
peso_permitido = peso > 50

print("O doador pode doar? ", idade_permitida and peso_permitido)