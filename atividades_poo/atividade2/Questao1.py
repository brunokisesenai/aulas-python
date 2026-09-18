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
            print(f'Estoque restante: {self.__quantidade_estoque()}')
        else:
            print(f'Estoque atual: {self.__quantidade_estoque()}')
            print(f"Estoque {venda}")
            print("Estoque insuficiente")



    def aplicar_desconto(self, desconto, __preço):
        desconto = int(input("Digite o valor do desconto aplicado ao produto: "))
        valor_venda = __preço - desconto
        print(f"O valor do final do produto foi {valor_venda}")


    def exibir_resumo(self, resumo):
        self.resumo = resumo
        print(resumo)



meu_produto = Produto("Notebook", "5000", 50)
print(meu_produto.__dict__)
meu_produto.adicionar_estoque(-50)
print(meu_produto.__dict__)




