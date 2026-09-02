#Crie um algoritmo que faça um formulário em que o usuário digite seu nome, sua idade e se ele tem plano de saúde (True ou False)
#O seu sistema deve retornar em um único print todas as informações e se ele for menor de idade ou idoso ou se não tiver plano de saúde, que ele não será aceito no nosso formulário.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
planodesaude = bool(input("Digite sim se possui planodesaude, caso contrário aperte enter apenas: "))
formularioaceito = (idade >= 18 and idade < 65 and planodesaude == True)

print("Seu nome é:", nome, ", você possui", idade, "anos de idade. ", "Tem plano de saúde?", planodesaude, " Você foi aceito? ", formularioaceito)