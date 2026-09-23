#CLASSE PAI

from abc import ABC, abstractmethod
class CalculoDeFrete(ABC):
    @abstractmethod
    def calcular_frete(self, distancia, valor, prazo):
        pass

    def calcular_tempo(self, prazo):
        print(f"O prazo de entrega é de {prazo} horas. ")