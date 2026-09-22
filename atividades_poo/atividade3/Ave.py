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




gaviao = Ave("Sky", 2, 75, 120)

gaviao.voar()
gaviao.voar()
gaviao.emitir_som()
gaviao.exibir_resumo()
gaviao.alimentar(50)

