class ItemPedido:
    def __init__(self, descricao, valor):
        self.descricao = str(descricao)
        self.valor = float(valor)



class Mesa:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
       self.pedidos.append(pedido)


    def listar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido.descricao)
        try:
            for item in self.pedidos:
                print(item.descricao, item.valor)
        except Exception as erro:
                print(f"Erro inesperado: {erro}")
        finally:
                print("Finalizando execução do método")


    def somar_pedido(self):

        for pedido in self.pedidos:
            pedido.valor += pedido.valor
            print(f"O valor da conta foi de R$ {pedido.valor}")




pedido1 = ItemPedido(descricao="Macarrão", valor=30)
pedido2 = ItemPedido(descricao="Sushi", valor=80)
pedido3 = ItemPedido(descricao="Picanha", valor=100)

mesa1 = Mesa()
mesa1.adicionar_pedido(pedido1)
mesa1.adicionar_pedido(pedido2)
mesa1.listar_pedidos()
mesa1.somar_pedido()



mesa2 = Mesa()
mesa2.adicionar_pedido(pedido1)
mesa2.adicionar_pedido(pedido3)
mesa2.listar_pedidos()
mesa2.somar_pedido()



