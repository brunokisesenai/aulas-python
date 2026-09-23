from Animal import Animal
from Mamifero import Mamifero
from Ave import Ave

class Main:
    print("TESTES")



#TESTE 1
leao = Mamifero("Simba", 5, 70, 80)
leao.correr()
leao.emitir_som()
leao.exibir_resumo()
leao.alimentar(50)
leao.alimentar(-1000)

#TESTE 2
leao._nivel_fome = -999
leao._idade = -10
leao.exibir_resumo()

gaviao = Ave("Sky", 2, 75, 120)

gaviao.voar()
gaviao.voar()
gaviao.emitir_som()
gaviao.exibir_resumo()
gaviao.alimentar(50)