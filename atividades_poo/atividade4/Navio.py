# CLASSE FILHA
from CalculoDeFrete import CalculoDeFrete


class Navio(CalculoDeFrete):
    def iniciando(self):
        print(f"O valor da taxa será calculado baseado na distância e peso")

    def calcular_frete(self, distancia, valor, prazo, peso):
        self.distancia = distancia
        self.valor = self.distancia
        calculo = valor * distancia
        if distancia >= 0:
            print(f"O Valor do frete do navio é de R$ {valor} por km")
            print(f"O valor total do frete para {self.distancia} km é de R$ {calculo}.")
        else:
            print(f"Erro: Distância inválida!")

    def descarregar(self, distancia, valor, prazo, peso):
        calculo = distancia * valor
        taxa = calculo * 1.1

        if peso >= 500:
            print(f"Para descarregar cargas com peso acima de {peso} kg, é obrigatório o pagamento de taxa portuária no valor de 10% do valor do frete.")
            print (f"O valor da taxa neste caso é de R$ {taxa}.")
        else:
            print("Não é necessário pagar a taxa portuária para descarregar.")



