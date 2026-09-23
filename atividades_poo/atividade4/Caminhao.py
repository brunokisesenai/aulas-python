#CLASSE FILHA
from CalculoDeFrete import CalculoDeFrete


class Caminhao(CalculoDeFrete):
    def iniciando(self):
        print(f"O valor do frete será calculado baseado no peso e distância")

    def calcular_frete(self, distancia, valor, prazo):
        print(f"O Valor do frete do caminhão é de R$ {valor} por km")
        self.distancia = distancia
        self.valor = self.distancia * 5
        print(f"O valor do frete para {self.distancia} km é de R$ {valor}.")


frete = Caminhao()
frete.calcular_frete(50, 100, 30)

