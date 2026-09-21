from aulas.poo.heranca.exemplo1.diretoria.Coordenacao import Coordenacao


class Sala(Coordenacao):
    def __init__(self, laboratorio, tipo, professores, cursos, alunos):
        super().__init__(professores, cursos, alunos)
        self.__laboratorio = laboratorio
        self.__tipo = tipo


    def ter_aula(self):
        print(f"Aula de: {self.cursos}"
              f"\nNo laboratório de {self.__tipo}"
              f"\nCom o professor: {self.excolher_professores[0]}"
              f"\nCom os alunos: {self.alunos}")
        for aluno in self.alunos:
            print(aluno)


sala_1 = Sala("Lab 7",
              "Tecnologia",
              "Joao",
              "Python",
              ["Fulano", "Beltrano", "Ciclano"])


sala_1.ter_aula()
