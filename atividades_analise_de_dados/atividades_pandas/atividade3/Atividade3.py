#Leia todos os dados do arquivo dados_despadronizados.csv  e faça a formatação para aceitar todos os CPFs, números e salários.
#Depois dos dados validados, escreva um novo documento dados_padronizados.csv com os valores das colunas formatadas, e também delas validadas(booleano).
#COLUNAS DESEJADAS: nome, cpf, cpf_formatado, cpf_valido, numero, numero_formatado, numero_valido, salario, salario_formatado
#Utilize os metotos feitos em sala de aula para formatar os dados usando o .str e .replace.
#DESAFIO EXTRA: criar uma nova coluna contendo o salário anual de cada funcionário.

import pandas as pd

#LENDO BANCO DE DADOS 'DADOS_DESPADRONIZADOS.CSV'
#df = pd.read_csv("dados_despadronizados.csv",sep=";")


print("============== LENDO O ARQUIVO DADOS_DESPADRONIZADOS.CSV ===============")

df = pd.read_csv(
    "dados_despadronizados.csv",
    sep=None,
    engine="python",
    dtype=str,
    encoding="utf-8-sig"
)

# Exibe todos os registros no terminal
print("\n")
print(df.to_string(justify='center'))


print("\n\n============== CRIANDO O ARQUIVO DADOS_PADRONIZADOS.CSV ===============")

df.to_csv("dados_padronizados.csv",sep=";",index=False)
print("\nO arquivo foi criado com sucesso!")


print("\n\n============== FORMATANDO O CPF ===============")


dados = pd.read_csv(
    "dados_despadronizados.csv",
    dtype={
        "cpf": "string",
        "numero": "string",
        "salario": "string"
    },
    sep=None,
    engine="python",
    encoding="utf-8-sig"
)


dados.insert(2, "cpf_formatado", dados["cpf"].str.replace(r"\D", "", regex=True))
dados.insert(3, "cpf_validado", dados["cpf_formatado"].str.fullmatch(r"\d{11}"))

print(dados.to_string(index=False))


print("\n\n============== PRÓXIMO ===============")





print("\n\n============== PRÓXIMO ===============")




print("\n\n============== PRÓXIMO ===============")





print("\n\n============== PRÓXIMO ===============")






print("\n\n============== PRÓXIMO ===============")

