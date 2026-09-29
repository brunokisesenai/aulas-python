# CLASSE PAI:


from abc import ABC, abstractmethod

class Transporte(ABC):


    def iniciar_processo(self):
        print("Sistema central: iniciando cálculo de frete...")


    @abstractmethod
    def calcular_frete(self, distancia, peso):
        pass