#QUESTÃO 4

mes = input("Digite o número correspondente ao mês em que estamos (De 1 a 12): ")

match mes:
    case "1" | "2" | "12":
        print("Estamos no Verão")
    case "3" | "4" | "5":
        print("Estamos no Outono")
    case "6" | "7" | "8":
        print("Estamos no Inverno")
    case "9" | "10" | "11":
        print("Estamos na Primavera")
    case _:
        print("Mês inválido")