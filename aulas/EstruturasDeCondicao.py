#IF e ELSE  ->  SE e SENÃO


#CASE SENSITIVE  ->  E != e

#if 1 ==1: #executa SE a resposta boleana for True
#    print("Verdadeiro")

#Exemplo:
#print("Menores de idade e idosos não podem entrar!")
#idade = int(input("Digite sua idade: "))

#if idade >= 18:
    #print("Acesso liberado")
#    if idade >= 65:
#        print("Desculpa, senhor. Idosos não podem entrar!")
#    else:
#        print("Acesso liberado")
#else:
#    print("Acesso negado")


#ELIF - else + if

#print("Menores de idade e idosos não podem entrar!")
#idade = int(input("Digite sua idade: "))

#if idade >= 18:
    #print("Acesso liberado")
#    if idade >= 65:
#        print("Desculpa, senhor. Idosos não podem entrar!")
#    else:
#        print("Acesso liberado")
#elif idade <5:
#    print("Além de não entrar, você não pode andarr sozinho")
#else:
#    print("Acesso negado")

    #EXEMPLO 2:
#nome = input("Digite seu nome: ")

#if nome == "":
#    print("Por favor, digite um nome válido.")
#elif nome == "Bruno":
#    print("Olha só! O dono da balada chegou")
#else:
#    print("Olá, "+ nome + "! Seja bem vindo a nossa balada.")



#MATCH CASE / SWITCH CASE:

#print("1 + 1 é igual a:\na)1\nb)2\nc)3\nd)4\ne)5")

#primeira_resposta = input ("Digite a resposta correta: ")
#if primeira_resposta == "a":
#    print("Resposta errada")
#elif primeira_resposta == "b":
#    print("Resposta correta")
#elif primeira_resposta == "c":
#    print("Resposta errada")
#elif primeira_resposta == "d":
#    print("Resposta errada")
#elif primeira_resposta == "e":
#    print("Resposta errada")

#primeira_resposta = input ("Digite a resposta correta: ")
#match primeira_resposta: #espera um string
#    case 'a':
#        print("Resposta incorreta")
#    case 'b':
#        print("Resposta correta")
#    case 'c':
#        print("Resposta errada")
#    case 'd':
#        print("Resposta errada")
#    case 'e':
#        print("Resposta errada")
#    case _: # significa valor default, ou seja, valor padrão
#        print("Resposta inválida")


#VÁRIAS OPÇÕES EM UM CASE

dia = input("Digite o dia dessa semana: ")

match dia:
    case "sábado" | "domingo":
        print("Esse dia é em um FINAL DE SEMANA")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Esse dia é DURANTE A SEMANA")