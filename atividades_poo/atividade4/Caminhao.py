#CLASSE FILHA
from CalculoDeFrete import CalculoDeFrete


class Caminhao(CalculoDeFrete):
    def iniciando(self):
        print(f"O valor do frete será calculado baseado no peso e distância")

    def calcular_frete(self, distancia, valor, prazo):
        self.distancia = distancia
        self.valor = valor
        calculo = valor * distancia
        if distancia >= 0:
            print(f"O Valor do frete do caminhão é de R$ {valor} por km")
            print(f"O valor total do frete para {self.distancia} km é de R$ {calculo}.")
        else:
            print(f"Erro: Distância inválida!")

    def parada(self, distancia, valor, prazo):
        self.distancia = distancia
        self.prazo = prazo
        self.valor = valor
        if (distancia >= 500) or (prazo >= 8):
            print(f"Se o motorista tiver que dirigir mais que 500 km ou mais que 8 horas, ele terá que efetuar uma parada de, pelo menos, 2h para descanso.")
        else:
            print(f"O motorista não precisa descansar!")

