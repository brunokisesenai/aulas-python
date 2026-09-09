# QUESTÃO 2

senha_fixa = 123456
senha = int(input("Digite sua senha: "))

while senha != senha_fixa:
    print("Senha incorreta. Tente novamente")
    senha = int(input("Digite sua senha: "))

print("Acesso permitido!")