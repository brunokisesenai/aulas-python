#  QUESTÃO 1

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque


    def adicionar_estoque(self, __quantidade_estoque):
        estoque_adicionado = int(input("Digite a quantidade de produtos a serem adicionados: "))
        estoque = estoque_adicionado + __quantidade_estoque
        print(f"Foram adicionados {estoque_adicionado} unidades do produto ao estoque. O saldo atual é de {estoque} unidades.")


    def realizar_venda(self, __quantidade_estoque):
        venda = int(input("Digite a quantidade de produtos vendidos: "))
        estoque_venda = __quantidade_estoque - venda
        print(f"Foram vendidos {estoque_venda} unidades do produto. O saldo atual é de {estoque_venda} unidades.")


    def aplicar_desconto(self, desconto, __preço):
        desconto = int(input("Digite o valor do desconto aplicado ao produto: "))
        valor_venda = __preço - desconto
        print(f"O valor do final do produto foi {valor_venda}")


    def exibir_resumo(self, resumo):
        self.resumo = resumo
        print(resumo)


produto_dados = Produto("Notebook", "5000", 100)
print(produto_dados.nome)
print(produto_dados.preco)
print(produto_dados.quantidade_estoque)




