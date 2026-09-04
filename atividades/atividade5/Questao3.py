#QUESTÃO 3

turno = input("Digite o turno em que o aluno estuda ('M' ou 'm' para matutino / 'V' ou 'v' para vespertino / 'N' ou 'n' para noturno): ")
match turno:
    case "M" | "m":
        print("Bom dia!")
    case "V" | "v":
        print("Boa tarde!")
    case "N" | "n":
        print("Boa noite!")
    case _:
        print("Turno inválido")