

class ContaBancaria:  #nome da classe
    def __init__(self, titular, saldo):  #metodo construtor
        self.titular = titular  #se.fatributo = valor do parametro
        self.__saldo = saldo


        #metodos Getters e Setters (Get = Pegar e Set = Inserir)


    def get_titular(self):
        senha = 1234
        senha_digitada = int(input("(GET) Digite sua senha: "))

        if senha == senha_digitada:
            return self.titular
        else:
            return "Senha incorreta!"

    def set_titular(self, novo_titular):
        senha = 1234
        senha_digitada = int(input("(SET) Digite sua senha: "))

        if senha == senha_digitada:
            self.titular = novo_titular
            return self.titular
        else:
            return "Senha incorreta!"




conta_banco = ContaBancaria("Bruno", 10000)
print(conta_banco.titular)  #Acesso diretamento o atributo
print(conta_banco.get_titular())

#conta_banco.titular = 'Fulano'  # Acesso diretamento o atributo... não recomendável
print(conta_banco.get_titular())

conta_banco.set_titular("Ciclano")  #modificando por metodo
print(conta_banco.get_titular())




class ContaBancariaCorreta:
    def __init__(self, titular, saldo): # LÓGICA UTILIZADA NO PYTHON de GET e SET
        self.titular = titular
        self.__saldo = saldo  #private

    @property  # anotation  ->  anotação
    def saldo(self):  #funcionar como o GET
        print("Acessando a informação do saldo...")
        return self.__saldo

    @saldo.setter   # criando um novo setter no metodo
    # quando o usuário digitar objeto.saldo acessa o metodo
    def saldo(self, novo_saldo):  #funciona como o SET
        self.__saldo = novo_saldo

    def sacar(self, valor_saque):
        if valor_saque <= self.__saldo:
            self.saldo -= valor_saque
            print(f"Quantidade retirada: {valor_saque}")
            print(f"Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente!")



usuario_banco_correto = ContaBancariaCorreta("Joao", 500)
print(usuario_banco_correto.saldo())

usuario_banco_correto.saldo = 5000
print(usuario_banco_correto.saldo)
print(usuario_banco_correto.__dict__)














