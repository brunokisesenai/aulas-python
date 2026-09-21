from Gato import Gato
from Animal import Animal
from Cachorro import Cachorro

class Main:
    print("INICIANDO CLASSE PRINCIPAL")

    gato1 = Gato(2, nome = "Tom", regiao ="Brasil")
    gato1.comer()
    gato1.dormir()
    gato1.mostraIdade()
    gato1.cospePelo()

    cachorro1 = Cachorro(3, "Zeus", "Alemanha")
    cachorro1.comer()
    cachorro1.dormir()
    cachorro1.mostraIdade()
    cachorro1.latir()



    animal = Animal(idade = 2, tipo = "BoladePelo")

