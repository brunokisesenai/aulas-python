# POO  ->  Programação Orientada a Objetos

# Toda classe precisa da palavra reservada class

class Aluno:  # toda classe começa com letra maiúscula
#    pass  # significado: eu vou escrever alguma coisa aqui futuramente
    nome_aluno = "João"  #atributo  ->  faz referência a uma variável de uma classe


    def __init__(self, nome_do_aluno, registro):  # metodo CONSTRUTOR
        # define a construção de um novo objeto
        # não se cria um objeto sem CONSTRUTOR
        # nome = novo atributo da classe
        # nome_do_aluno = parâmetro

        self.nome = nome_do_aluno  # é o mesmo que escrever nome = Aluno.nome_aluno
        self.registro = registro

        # todos os alunos, OBRIGATORIAMENTE, precisam ter nome e registro

    #METODO DE FORMATAÇÃO
    def __str__(self):
        return print(self.nome, self.registro)


    def mostrarNomeAluno(self): #metodo que usa os valores de alguma instância
       # Todos os metodos dentro de uma classe precisam de self
       print(self.nome_aluno)  # uso o self para pegar um valor dentro da classe





# instância da variável nome
# instância = referência
# quando eu faço a instância eu insiro o valor do ATRIBUTO DO OBJETO
# aluno1 = objeto
aluno1 = Aluno("João", registro = 11111)  # instância do objeto aluno1
aluno2 = Aluno("Fulano", registro = 22222)  # outra instância do objeto aluno2
aluno3 = aluno1  # criando um novo objeto, mas não cria instância nova
aluno4 = Aluno("", 0.0)


# nome_de_um_aluno = "Fulano"  #  fora da classe ocupa um espaço próprio

#print(aluno1.nome)
#print(aluno1.registro)
#print(aluno4)

# not compara valores vazios (None), ou que representam vazio
string = ""
numero_inteiro = 0
numero_quebrado = 0.0
lista = []
tupla = ()
boolean = False
vazio = None


if not aluno1.nome:
    print("Aluno não tem valor registrado como nome.")



