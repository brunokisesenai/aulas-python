#Questão 6: O Erro de Verificação (Análise e Correção de Código)

#senha_cadastrada = 1234
#senha_digitada = input("Digite sua senha: ")
#acesso_liberado = senha_cadastrada == senha_digitada
#print("Acesso liberado?", acesso_liberado)

senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)

#O erro acontece porque a senha cadastrada está no formato "int" e o input original da senha digitada está no formato "string". O erro pode ser corrigido formatando o tipo da senha digitada para "inteiro"