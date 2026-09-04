#QUESTÃO 1

codigo = input("Digite o código do produto desejado: ")

match codigo:
    case "1":
        print("Produto: Cachorro-quente\nPreço: R$10,00")
    case "2":
        print("Produto: Hambúrguer\nPreço: R$15,00")
    case "3":
        print("Produto: Batata Frita\nPreço: R$8,00")
    case "4":
        print("Produto: Refrigerante\nPreço: R$5,00")
    case _:
        print("Código inválido")