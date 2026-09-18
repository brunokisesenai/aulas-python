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
        else:
            print("Erro: quantidade inválida!")


    def realizar_venda(self, venda):
        if venda <= self.__quantidade_estoque:
            self.__quantidade_estoque -= venda
            print(f'Quantidade retirada: {venda}')
            print(f'Estoque restante: {self.__quantidade_estoque}')
        else:
            print(f'Estoque atual: {self.__quantidade_estoque}')
            print(f"Tentativa de retirada de {venda} unidades. Estoque insuficiente!!!")


    def aplicar_desconto(self, desconto):
        if desconto > 0:
            self.__preco -= desconto
            print(f"O valor final do produto com desconto de R$ {desconto}, foi de R$ {self.__preco}")

        else:
            print("Desconto inválido")


    def exibir_resumo(self, resumo):
        self.resumo = resumo
        print(resumo)



meu_produto = Produto("Notebook", 5000, 50)


#ADICIONAR PRODUTO
#print(meu_produto.__dict__)
#meu_produto.adicionar_estoque(-50)
#print(meu_produto.__dict__)

#meu_produto.__quantidade_estoque = -50
#meu_produto.__preco = -100
#print(meu_produto.__dict__)

#REALIZAR VENDA
#meu_produto.realizar_venda(10)
#meu_produto.realizar_venda(100)

#DESCONTO:
#meu_produto.aplicar_desconto(50)

#EXIBIR RESUMO:
#print(meu_produto.__dict__)


