#Questão 8: A Calculadora de Lucro da Empresa

produto = input("Digite o nome do produto: ")
custo = float(input("Digite o valor de custo do produto: R$ "))
venda = float(input("Digite o valor de venda: R$ "))
lucro = venda - custo

print("O produto é", produto, "e o lucro foi de R$", lucro, ". O lucro foi bom? ", lucro > 20)