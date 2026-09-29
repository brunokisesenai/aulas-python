
class ItemPedido:

    def __init__(self, descricao, valor):
        self.descricao = descricao

        try:
            self.valor = float(valor)

        except ValueError:
            raise ValueError(f"Erro: O valor para '{descricao}' deve ser estritamente numérico.")



class Mesa:

    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.pedidos = []

    def adicionar_pedido(self, item):
        self.pedidos.append(item)
        print(f"-> {item.descricao} adicionado à {self.numero_mesa}.")


    def somar_total(self):

        total = 0

        for item in self.pedidos:
            total += item.valor
        return total


    def fechar_conta(self, taxa_servico):

        print(f"\n========== EXTRATO - {self.numero_mesa} ==========")

        if len(self.pedidos) == 0:
            print("Nenhum pedido registrado.")
            print("Subtotal: R$ 0.00")
            print("Taxa de serviço: R$ 0.00")
            print("TOTAL A PAGAR: R$ 0.00")
            print("==========================================")
            return

        print("Itens consumidos:")

        for item in self.pedidos:
            print(f"- {item.descricao}: R$ {item.valor:.2f}")

        # Calcula o subtotal
        subtotal = self.somar_total()

        # Calcula o valor da taxa de serviço
        valor_taxa = subtotal * (taxa_servico / 100)

        # Calcula o total final
        total_final = subtotal + valor_taxa

        print("------------------------------------------")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print(
            f"Taxa de serviço ({taxa_servico}%): "
            f"R$ {valor_taxa:.2f}"
        )
        print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
        print("==========================================")

        # Limpa a lista de pedidos após o fechamento
        self.pedidos.clear()

        print(f"{self.numero_mesa} liberada para novos clientes.")


# ============================================================
# FUNÇÃO AUXILIAR
# ============================================================

def registrar_pedido_seguro(mesa, descricao, valor):

    try:
        # Tenta criar o item
        item = ItemPedido(descricao, valor)

        # Se não houver erro, adiciona o item à mesa
        mesa.adicionar_pedido(item)

    except ValueError as erro:
        # Captura o erro sem interromper o programa
        print(f"ALERTA DO SISTEMA: {erro}")


# ============================================================
# TESTES
# ============================================================

# 1. Instanciando a mesa

mesa1 = Mesa("Mesa 1")


# 2. Registrando pedidos válidos

registrar_pedido_seguro(
    mesa1,
    "Pizza Margherita",
    45.90
)

registrar_pedido_seguro(
    mesa1,
    "Refrigerante",
    8.50
)


# 3. Testando o Tratamento de Exceções

print("\n--- TESTANDO ENTRADA INVÁLIDA ---")

registrar_pedido_seguro(
    mesa1,
    "Pudim",
    "quinze"
)

registrar_pedido_seguro(
    mesa1,
    "Café",
    "5,50"
)


# 4. Adicionando outro pedido válido após os erros

registrar_pedido_seguro(
    mesa1,
    "Suco de Laranja",
    12.00
)


# 5. Fechando a conta com 10% de taxa

print("\n--- FECHAMENTO DA CONTA ---")

mesa1.fechar_conta(taxa_servico=10)


# 6. Verificando se a mesa foi limpa

print("\n--- VERIFICANDO STATUS DA MESA APÓS FECHAMENTO ---")

mesa1.fechar_conta(taxa_servico=10)


