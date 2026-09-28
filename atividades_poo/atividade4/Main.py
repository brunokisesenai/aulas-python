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
caminhao1 = Caminhao()
caminhao2 = Caminhao()
caminhao3 = Caminhao()
lote_caminhao = [caminhao1, caminhao2, caminhao3]

print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")

for item in lote:
    caminhao.calcular_frete(50, 100, 70, 200)
    # Chama o método que era abstrato, mas agora está implementado
    item.metodo_abstrato(argumento1, argumento2)
    print("-" * 30)
