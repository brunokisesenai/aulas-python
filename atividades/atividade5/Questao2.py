#QUESTÃO 2

letra = input("Digite uma letra (minúscula): ")

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Você digitou uma vogal")
    case _:
        print("Não é uma vogal")