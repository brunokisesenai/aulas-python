#CLASSE FILHA

from Animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, nivel_fome, envergadura_asas):
        super().__init__(nome = nome, idade = idade, nivel_fome = nivel_fome)
        self._envergadura_asas = envergadura_asas


    def voar(self):
        if self.nivel_fome <= 80:
            print(f"O {self.nome} voou com suas asas de {self._envergadura_asas} cm!")
            self.nivel_fome += 15
        else:
            print(f"Voo negado. O {self.nome} está cansado demais para voar")

    def emitir_som(self):
        print(f"O {self.nome} canta um som melodioso!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"A envergadura das asas é de {self._envergadura_asas} cm.")




ave1 = Ave("Canário", 10, 50, 80)

ave1.voar()
ave1.emitir_som()
ave1.exibir_resumo()
ave1.alimentar(50)

