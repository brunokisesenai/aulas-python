from CalculoDeFrete import CalculoDeFrete
from Caminhao import Caminhao
from Navio import Navio

class Main:
    print("TESTES")

print("-----------------TESTES CAMINHÃO---------------------")
caminhao = Caminhao()
caminhao.calcular_frete(50, 20, 30, 100)
caminhao.parada(50, 20, 7, 150)



print("-----------------TESTES NAVIO---------------------")
taxa = Navio()
taxa.iniciando()
taxa.calcular_frete(50, 100, 70, 200)
taxa.descarregar(50, 100, 70, 100)
taxa.calcular_frete(50, 100, 70, 150)

print("-----------------TESTES FINAIS---------------------")

# 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
# Descomente a linha abaixo para testar e provar que o Python bloqueia:
# objeto_generico = CalculoDeFrete()

# 2. Instanciando as Classes Filhas
obj1 = Caminhao()
obj2 = Navio()
