from Transporte import Transporte
from Caminhao import Caminhao
from Drone import Drone


def processar_lote(lista_de_objetos, distancia, peso):

    for item in lista_de_objetos:
        item.iniciar_processo()
        item.calcular_frete(distancia, peso)
        print("-" * 40)



"--------------------TESTES--------------------"


# 1. Tentativa de instanciar a Classe Abstrata
# DEVE GERAR ERRO:
#
# transporte = Transporte()
#
# O Python não permite criar um objeto diretamente
# de uma classe que possui métodos abstratos.


# 2. Instanciando as Classes Filhas

obj1 = Caminhao()
obj2 = Drone()


# 3. Criando um Lote de Processamento

lote = [obj1, obj2, obj1]


# 4. Processando em lote
# Demonstrando Abstração e Polimorfismo

print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")

processar_lote(lote, distancia=10, peso=1.5)


# ============================================================
# TESTE DA VALIDAÇÃO DO DRONE
# ============================================================

print("\n--- TESTANDO LIMITE DE PESO DO DRONE ---")

drone = Drone()

drone.iniciar_processo()
drone.calcular_frete(distancia=10, peso=5)
