def cadastrar_venda():
    vendedor = input("Digite o nome do vendedor: ")
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))

    with open("vendas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{vendedor}; {produto}; {valor:.2f}\n")



