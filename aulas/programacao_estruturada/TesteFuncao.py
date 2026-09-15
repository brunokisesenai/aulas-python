#ARQUIVO TesteFuncao.py

from aulas.programacao_estruturada.Funcoes import soma, olaUsuario

#Exemplo 1
#soma()
#subtracao()

"-------------------------------------------"


olaUsuario("Bruno", "44")

while True:
    valor = soma()
    print(valor)
    opcao = input("Quer finalizar? y/n")
    if opcao == 'y':
        break

print("Finalizando execução!")


