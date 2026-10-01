

def cadastrar_venda():
    vendedor = input("Digite o nome do vendedor: ")
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))

    with open("vendas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{vendedor}; {produto}; {valor:.2f}\n")

    print("Venda cadastrada")

cadastrar_venda()


def listar_vendas():
    try:
        with open("vendas.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                linha = linha.strip().split(";")

                print(f"Vendedor: {linha[0]}\nProduto: {linha[1]}\nValor: {linha[2]}")

    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print(f"Erro inesperado: {error}")
    finally:
        print("Base de dados analisada")


def somar_todas_as_vendas(valor_total = 0):
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha  = linha.strip().split(";")
            valor_produto = float(linha[2])
            valor_total += valor_produto
    return valor_total

def achar_vendedor():
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip().split(";")
            if linha[0] == "João":
                print(f"O João fez a venda de um{linha[1]}")

def modificar_venda():
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip().split(";")
            if linha[0] == "João" and float(linha[2]) == 600000:
                linha[1] == "Mansão"








#SIMULANDO UM SISTEMA FUNCIONAL

while True:
    finalizar = False
    print("SISTEMA DE COMPRAS\n\n")
    opcao = int(input("Escolha uma das opções\n"
                  "1) Cadastrar venda nova\n"
                  "2) Listar todas as vendas\n"
                  "3) Somar todas as vendas\n"
                  "4) Ver as vendas de um vendedor\n"    
                  "5) Modificar venda\n"
                  "6) Finalizar programa\n"))

    match opcao:
        case 1:
            cadastrar_venda()
        case 2:
            listar_vendas()
        case 3:
            print(somar_todas_as_vendas())
        case 4:
            print(achar_vendedor())
        case 5:
            print(modificar_venda())
        case _:
            print("Finalizando programa...")
            finalizar = True
            break





listar_vendas()

