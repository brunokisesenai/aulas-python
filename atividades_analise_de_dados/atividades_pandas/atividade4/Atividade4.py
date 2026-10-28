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


#print(df.to_string(index=False))


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


#print("\n\n============== FORMATANDO O SETOR ===============")


#dados_setor_formatado = (df["setor"]
#                              .str.replace(r"[^\d,.\-]", "", regex=True)
#                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
#                              .str.replace(r",",".", regex=False)
#                              )

#df.insert(6, "setor_formatado",dados_setor_formatado)


#print(df.to_string(index=False))



print("\n\n============== FORMATANDO AS DATAS ===============")

df_analise_estoque = df[["nome", "preco_formatado", "quantidade_formatada", "data_compra", "data_vencimento"]]
df_analise_estoque["data_vencimento"] = pd.to_datetime(
    df_analise_estoque["data_vencimentoo"],
    format="%d/%m/%Y")
df["data_vencimento"] = df["data_vencimento"].fillna(27/10/2026)



print(df.to_string(index=False))
















