#COMPOSIÇÃO

class Carro:
    def __init__(self, modelo, motor):
        self.__modelo = modelo
        self.motor = Motor(motor)  #instanciando a classe

    def acelerar(self):
        print(f"O carro {self.__modelo} acelerou")

    def quebrar(self):
        print(f"Carro {self.__modelo} quebrou")
        self.motor.estado_motor = "quebrado"


class Motor:
    def __init__(self, tipo_motor):
        self.__tipo_motor = tipo_motor
        self.__estado_motor = "funcionando"

    @property
    def tipo_motor(self):
        return self.__tipo_motor

    @property
    def estado_motor(self):
        return self.__estado_motor


    @estado_motor.setter
    def estado_motor(self, value):
        self.__tipo_motor = value





carro_joao = Carro("Camaro", "V8")
print(carro_joao.__dict__)
carro_joao.acelerar()
carro_joao.quebrar()
print(f"Estado atual do carro: {carro_joao.estado_motor}")











