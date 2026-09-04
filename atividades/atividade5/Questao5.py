#QUESTÃO 5

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: " ))
operacao = input("Escolha o símbolo da operação aritmética que deseja realizar (+, -, *, /): ")

match operacao:
    case "+":
        print("A soma dos números é igual a: ", numero1 + numero2)
    case "-":
        print("A subtração dos números é igual a: ", numero1 - numero2)
    case "*":
        print("A multiplicação dos números é igual a: ", numero1 * numero2)
    case "/":
        print("A divisão do primeiro número pelo segundo é igual a: " , numero1 / numero2)
    case _:
        print("Operação inválida!")
