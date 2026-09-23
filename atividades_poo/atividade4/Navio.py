# CLASSE FILHA
from CalculoDeFrete import CalculoDeFrete


class Navio(CalculoDeFrete):
    def iniciando(self):
        print(f"O valor do frete será calculado baseado no peso e distância")

    def calcular_taxa(self, distancia, valor, prazo):
        print(f"O Valor do frete do caminhão é de R$ {valor} por km")
        self.distancia = distancia
        self.valor = self.distancia * 20
        print(f"O valor do frete para {self.distancia} km é de R$ {valor}.")


taxa = Navio()
taxa.calcular_taxa(50, 100, 30)
