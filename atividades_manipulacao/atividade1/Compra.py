#RESPOSTA DA ATIVIDADE

nome = str(input("Digite o nome do usuário/cliente: "))
print(f"O nome do cliente é {nome}.")
print("LISTA DE COMPRAS")

lista_de_compras = []
total = 0


while True:
    nome = input("Digite 'fim' para finalizar."
                 "\nDigite o nome do produto: ")
    if nome == 'fim':
        break

    preco = float(input("Digite o valor desse produto: R$"))

    total += preco

    # adicionando uma LISTA dentro de uma LISTA

    lista_de_compras.append([nome,preco])

with open("lista_de_compras.txt", "w", encoding='utf-8') as arquivo:
    arquivo.write("LISTA DE COMPRAS\n\n")



    for produto in lista_de_compras:
        #print(f"{produto[0]}: {produto[1]}")
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(f"Produto: {nome_produto}: R$ {preco_produto:.2f}\n")


    arquivo.write(f"Total a pagar: R${total:.2f}\n")
















