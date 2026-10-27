import pandas as pd

#LENDO BANCO DE DADOS 'DADOS_DESPADRONIZADOS.CSV'
#df = pd.read_csv("dados_despadronizados.csv",sep=";")


print("============== LENDO O ARQUIVO ESTOQUE_SUPERMERCADO.CSV ===============")

df = pd.read_csv(
    "estoque_supermercado.csv",
    sep=None,
    engine="python",
    dtype=str,
    encoding="utf-8-sig"
)

# Exibe todos os registros no terminal
print("\n")
print(df.to_string(justify='center'))