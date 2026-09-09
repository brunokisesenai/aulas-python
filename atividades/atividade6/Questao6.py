#QUESTÃO 6

print("Descubra o número secreto!")
numero_secreto = 20
tentativas = 1

numero = int(input("Digite um número: "))

while numero != numero_secreto:
    numero = int(input("Digite um novo número: "))
    tentativas += 1

print("Parabéns! Você acertou o número secreto em", tentativas,"tentativas!")
