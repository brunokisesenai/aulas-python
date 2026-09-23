# CLASSE FILHA
from CalculoDeFrete import CalculoDeFrete


class Navio(CalculoDeFrete):
    def iniciando(self):
        print(f"O valor da taxa será calculado baseado na distância e peso")

    def calcular_frete(self, distancia, valor, prazo):
        print(f"O Valor da taxa do navio é de R$ {valor} por km")
        self.distancia = distancia
        self.valor = self.distancia * 20
        self.prazo = prazo
        print(f"O valor do frete para {self.distancia} km é de R$ {valor}.")



taxa = Navio()
taxa.iniciando()
taxa.calcular_frete(50, 100, 70)
