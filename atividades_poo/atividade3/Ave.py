#CLASSE FILHA

from Animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, envergadura_asas):
        super().__init__(nome, idade)
        self._envergadura_asas = envergadura_asas