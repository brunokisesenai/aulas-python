#  QUESTÃO 1

class Produto:

#CONSTRUTOR:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque


#MÉTODOS:

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
            print(f"Foram adicionados {quantidade} unidades ao estoque. O estoque atual é de {self.__quantidade_estoque} unidades.")
        else:
            print("Erro: quantidade inválida!")


    def realizar_venda(self, venda):
        if venda <= self.__quantidade_estoque:
            self.__quantidade_estoque -= venda
            print(f'Quantidade retirada: {venda}')
            print(f'Estoque restante: {self.__quantidade_estoque}')
        else:
            print(f'Estoque atual: {self.__quantidade_estoque}')
            print(f"Tentativa de retirada de {venda} unidades. Venda negada. Saldo insuficiente.!!!")


    def aplicar_desconto(self, desconto):
        if desconto > 0 and desconto <= 80:
            self.__preco *= (desconto/100)
            print(f"O valor final do produto com desconto de {desconto} %, foi de R$ {self.__preco}")
        else:
            print(f"Erro: Desconto inválido!. Valor do produto: R$ {self.__preco}")


    def exibir_resumo(self, resumo):
        self.resumo = resumo
        print(f"Resumo: existem {self.__quantidade_estoque} unidades do produto {self.__nome} com valor de R$ {self.__preco} no estoque.")



meu_produto = Produto("Notebook", 5000, 50)


#ADICIONAR PRODUTO
#print(meu_produto.__dict__)
#meu_produto.adicionar_estoque(50)
#print(meu_produto.__dict__)
#meu_produto.adicionar_estoque(-50)
#meu_produto.__quantidade_estoque = -50
#meu_produto.__preco = -100
#print(meu_produto.__dict__)

#REALIZAR VENDA
#meu_produto.realizar_venda(10)
#meu_produto.realizar_venda(999)

#DESCONTO:
#meu_produto.aplicar_desconto(90)

#EXIBIR RESUMO:
#meu_produto.exibir_resumo(0)


