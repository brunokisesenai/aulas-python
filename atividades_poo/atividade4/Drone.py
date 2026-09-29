# CLASSE FILHA 2

from Transporte import Transporte

class Drone(Transporte):

    def calcular_frete(self, distancia, peso):
        # O drone aceita cargas de até 2 kg
        if peso <= 2:
            # O drone cobra R$ 20,00 por quilômetro
            valor = distancia * 20

            print(f"Transporte: Drone")
            print(f"Distância: {distancia} km")
            print(f"Peso: {peso} kg")
            print(f"Frete calculado: R$ {valor:.2f}")

            return valor

        else:
            print("Transporte: Drone")
            print(f"Peso: {peso} kg")
            print("ERRO: O drone transporta cargas de até 2 kg.")

            return None



