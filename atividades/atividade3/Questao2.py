#Questão 2: A Fábrica de Caixas (Operador de Módulo)
#Uma fábrica empacota maçãs em caixas que cabem exatamente 12 unidades. Crie um programa que pergunte ao usuário a quantidade total de maçãs colhidas no dia. Utilizando o operador de módulo (%), calcule e exiba na tela quantas maçãs sobrarão fora das caixas (ou seja, o resto da divisão por 12).

total_macas = int(input("Digite o total de maçãs colhidas no dia: "))
numero_caixas = int(total_macas / 12)
macas_sobra = total_macas - (numero_caixas * 12)

print("Número de caixas:" , numero_caixas)
print("Sobraram" , macas_sobra, "maçãs fora da caixa")