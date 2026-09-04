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

print("Menores de idade e idosos não podem entrar!")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    #print("Acesso liberado")
    if idade >= 65:
        print("Desculpa, senhor. Idosos não podem entrar!")
    else:
        print("Acesso liberado")
elif idade <5:
    print("Além de não entrar, você não pode andarr sozinho")
else:
    print("Acesso negado")

    #EXEMPLO 2:
nome = input("Digite seu nome: ")

if nome == "":
    print("Por favor, digite um nome válido.")
elif nome == "Bruno":
    print("Olha só! O dono da balada chegou")
else:
    print("Olá, "+ nome + "! Seja bem vindo a nossa balada.")