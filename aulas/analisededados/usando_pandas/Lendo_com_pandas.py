import pandas as pd


print("LENDO DADOS SALVOS COM LISTA")
df = pd.read_csv("dados_da_lista.csv")
print(df)

print("LENDO DADOS SLAVOS COM DICIONÁRIO")
df = pd.read_csv("dados_do_dicionario.csv")
print(df)