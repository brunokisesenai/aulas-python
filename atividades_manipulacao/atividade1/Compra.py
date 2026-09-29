#RESPOSTA DA ATIVIDADE

cliente = str(input("Digite o nome do usuário/cliente: "))
print(f"O nome do cliente é {cliente}.")
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
    arquivo.write("LISTA DE COMPRAS\n\n"
                  f"Cliente: {cliente}\n\n")



    for produto in lista_de_compras:
        #print(f"{produto[0]}: {produto[1]}")
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(f"Produto: {nome_produto}: R$ {preco_produto:.2f}\n")


    arquivo.write(f"Compra processada com sucesso! Valor cobrado: R${total:.2f}\n")


with open("lista_de_compras.txt", 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    posicao = texto.find("Compra")
    print(posicao)
    total_a_pagar = texto[posicao:posicao+53]
    print(f"O total a pagar é R$ {total_a_pagar}.")













