#RESPOSTA DA ATIVIDADE

cliente = str(input("Digite seu nome para inciar a compra: "))
print(f"O nome do cliente é {cliente}.")
print("LISTA DE COMPRAS")

pagamento = []
total = 0


while True:
    nome = input("Digite 'fim' para finalizar."
                 "\nDigite o nome do produto: ")
    if nome == 'fim':
        break

    preco = float(input("Digite o valor desse produto: R$"))

    total += preco

    # adicionando uma LISTA dentro de uma LISTA

    pagamento.append([nome,preco])

print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding='utf-8') as arquivo:
    arquivo.write("LISTA DE COMPRAS\n\n"
                  f"Cliente: {cliente}\n\n")



    for produto in pagamento:
        #print(f"{produto[0]}: {produto[1]}")
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(f"Produto: {nome_produto}: R$ {preco_produto:.2f}\n\n")


    arquivo.write(f"Compra processada com sucesso! Valor cobrado: R${total:.2f}\n")

print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    posicao = texto.find("Compra")
    print(posicao)
    total_a_pagar = texto[posicao:posicao+53]
    print(f"O total a pagar é R$ {total}.")













