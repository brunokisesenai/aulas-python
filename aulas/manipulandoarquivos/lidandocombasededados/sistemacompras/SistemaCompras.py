def cadastrar_venda():
    vendedor = input("Digite o nome do vendedor: ")
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))

    with open("vendas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{vendedor}; {produto}; {valor:.2f}\n")

    print("Venda cadastrada")

cadastrar_venda()


def lista_vendas():
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

