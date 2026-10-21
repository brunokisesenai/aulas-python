import pandas as pd


print("LENDO DADOS SALVOS COM LISTA")
df = pd.read_csv("dados_da_lista.csv")
print(df)

#nome = input("Digite um nome que queira procurar na base de dados: ")

#print(df[df["nome"] == nome])

#idade = int(input("Digite um limite de idade"))

#print(df[df["idade"] == idade])


#buscando com operador 'and'
print(df[
          (df['idade'] > 20) & (df['idade'] < 25)
      ])

#buscando com operador 'or'
print(df[
          (df['idade'] > 20) | (df['idade'] < 30)
      ])






#print("LENDO DADOS SALVOS COM DICIONÁRIO")
#df = pd.read_csv("dados_do_dicionario.csv")
#print(df)
#print(df[["nome", "idade"]])
