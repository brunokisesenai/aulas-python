# QUESTÃO 7

orcamento = 500
print("Seu orçamento é de R$ 500,00")
gasto = int(input("Digite o valor do gasto: "))
saldo = orcamento - gasto

while saldo > 0:
    print("Seu saldo atual é: R$", saldo)
    gasto = int(input("Digite o valor do novo gasto: "))
    saldo = saldo - gasto

print("Atenção! Você ficou sem saldo ou estorou seu orçamento!")

