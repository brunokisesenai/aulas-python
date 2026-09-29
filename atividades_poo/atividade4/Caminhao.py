#CLASSE FILHA 1

from Transporte import Transporte

class Caminhao(Transporte):

    def calcular_frete(self, distancia, peso):
        # O caminhão cobra R$ 5,00 por quilômetro
        valor = distancia * 5

        print(f"Transporte: Caminhão")
        print(f"Distância: {distancia} km")
        print(f"Peso: {peso} kg")
        print(f"Frete calculado: R$ {valor:.2f}")

        return valor

