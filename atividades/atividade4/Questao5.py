#QUESTÃO 5

idade = int(input("Digite sua idade: "))
vip = int(input("Possui convite VIP? Se 'sim', digite 1. Se 'não', digite 0: "))
organizador = int(input("Você é um dos organizadores do evento? Se 'sim', digite 1. Se 'não', digite 0: "))
if ((idade >= 18 and vip == 1) or (organizador == 1)):
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:
    print("Entrada NEGADA. Você não atende aos requisitos")
