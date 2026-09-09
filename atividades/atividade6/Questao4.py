# QUESTÃO 4

print("1 - Mostrar saudação\n2 - Sair do programa")

escolha = input("Digite sua escolha: ")

while escolha == "1":
    print("Olá! Seja muito bem-vindo(a)!")
    escolha = input("Digite sua escolha: ")
while escolha != "1" and escolha != "2":
    print("Opção inválida!")
    escolha = input("Digite sua escolha: ")
if escolha == "2":
    print("Programa encerrado!")
   


