import pandas as pd


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

print("\n\n============== FORMATANDO O PREÇO ===============")

dados_preco_formatado = (df["preco"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",",".", regex=False)
                              )
dados_preco_formatado = pd.to_numeric(dados_preco_formatado, errors="coerce")
df.insert(2, "preco_formatado",dados_preco_formatado)
df["preco_formatado"] = df["preco_formatado"].fillna(0.0)


print(df.to_string(index=False))


print("\n\n============== FORMATANDO A QUANTIDADE ===============")


dados_quantidade_formatada = (df["quantidade"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",",".", regex=False)
                              )
dados_quantidade_formatada = pd.to_numeric(dados_quantidade_formatada, errors="coerce")
df.insert(4, "quantidade_formatada",dados_quantidade_formatada)
df["quantidade_formatada"] = df["quantidade_formatada"].fillna(0)
df["quantidade_formatada"] = df["quantidade_formatada"].astype(int)


print(df.to_string(index=False))







