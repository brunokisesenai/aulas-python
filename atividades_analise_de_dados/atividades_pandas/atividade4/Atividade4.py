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
                              .astype(float)
                              )

df.insert(2, "preco_formatado",dados_preco_formatado)
print(df["preco_formatado"])


print(df.to_string(index=False))















