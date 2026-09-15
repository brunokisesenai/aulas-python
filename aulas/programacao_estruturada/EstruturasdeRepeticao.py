# REPETIÇÃO WHILE  ->  Enquanto
# ESTRUTURAS DE REPETIÇÃO
# LAÇOS DE REPETIÇÃO
# LOOP

#EXEMPLO 1: NÃO RODAR, POIS TRAVA O PROGRAMA!!!
#ano_nascimento = 2004
#ano_final = 2077

#idade = 0
#while ano_nascimento <= ano_final:    (ou while True:)
#    idade += 1
#    print(idade)
#    break (PARA O PROGRAMA)

"------------------------------------------------------------------------"
#EXEMPLO 2:

#ano_nascimento = 2004
#ano_final = 2077

#print("O ano atual é: ", ano_nascimento)

#idade = 0
#while ano_nascimento <= ano_final:
#    idade += 1
#    print(idade)

#    if (ano_nascimento == ano_final):
#        print("O ano atual é: ", ano_nascimento)
#    ano_nascimento += 1


"-------------------------------------------------------------------------"

#seu_nome = input("Digite seu nome: ")

#while seu_nome != "Bruno":
#    print("Pessoa não encontrada..")
#    seu_nome = input("Digite seu nome novamente: ")
#print("Bem vindo, Bruno!")

"----------------------------------------------------------------------------"

#tentativas = 3
#while True:
#        print(f"Você tem {tentativas} tentativas.")
#        opcao = input("Escolha uma opção: ")

#        if opcao == "b":
#             print("Você ganhou!")
#             break

#        elif tentativas == 1:
#            print("Você perdeu!")
#            break

#        else:
#            tentativas -= 1


"------------------------------------------------------------------------------"

tentativas = 3
fichas = 1
while fichas != 0: #sistea da maquina do fliperama
    print(f"Você tem  {fichas}, quantidade de fichas")
    while True: #sistea do jogo do fliperama
        print(f"Você tem {tentativas} tentativas.")
        opcao = input("Escolha uma opção: ")

        if opcao == "b":
             print("Você ganhou!")
             break

        elif tentativas == 1:
            print("Você perdeu!")
            break

        else:
            tentativas -= 1

    fichas -=1
    if fichas <= 0:
        break
