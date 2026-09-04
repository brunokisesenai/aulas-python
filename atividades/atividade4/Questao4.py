#QUESTÃO 4

saldoinicial = 500
saque = float(input("Digite o valor que deseja sacar: "))
saldofinal = saldoinicial - saque

if saldoinicial >= saque:
    print("Saque realizado com sucesso!")
    print("Saldo atual: R$ ", saldofinal)
else:
    print("Saldo insuficiente para realizar esta operação")