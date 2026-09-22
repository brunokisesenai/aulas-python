from Gato import Gato
from Animal import Animal
from Cachorro import Cachorro
from aulas.poo.heranca.exemplo2.Baleia import Baleia
from aulas.poo.heranca.exemplo2.CachorroDomestico import CachorroDomestico


class Main:
    print("INICIANDO CLASSE PRINCIPAL")

    gato1 = Gato(2, nome = "Tom", regiao = "Brasil")
    gato1.comer()
    gato1.dormir()
    gato1.mostraIdade()
    gato1.cospePelo()
    gato1.mostraIdadeDoGato()


    cachorro1 = Cachorro(3, "Zeus", "Alemanha")
    cachorro1.comer()
    cachorro1.dormir()
    cachorro1.mostraIdade()
    cachorro1.latir()
    cachorro1.aniversario()

    cachorro_domestico = CachorroDomestico
    cachorro_domestico.nome = "Max"
    print(f"O nome do seu cachorro doméstico é {cachorro_domestico.nome}")





    baleia = Baleia("Gigante", 20, "Brasil")
    baleia.comer()
    baleia.dormir()
    baleia.mostraIdade()


