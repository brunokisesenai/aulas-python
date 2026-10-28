import pandas as pd
from pandas.compat.numpy.function import validate_logical_func

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
media_precos = df["preco_formatado"].mean()
df["preco_formatado"] = df["preco_formatado"].fillna(media_precos)

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


print("\n\n============== FORMATANDO O SETOR ===============")

dados_setor_formatado = (df["setor"]
                        .str.strip()
                        .str.lower()
                        .fillna("sem setor")
                        .replace("", "sem setor")
)

df.insert(6, "setor_formatado", dados_setor_formatado)

print("\n")
print(df.to_string(index=False))



print("\n\n============== FORMATANDO AS DATAS ===============")

df_analise_estoque = df[["nome", "preco_formatado", "quantidade_formatada", "setor_formatado", "data_compra", "data_vencimento"]]
df_analise_estoque["data_vencimento"] = pd.to_datetime(
    df_analise_estoque["data_vencimento"],
    format="%d/%m/%Y")
df["data_vencimento"] = df["data_vencimento"].fillna("27/10/2026")

print("\n")
print(df.to_string(index=False))


print("\n\n============== PRODUTOS VENCENDO ESTA SEMANA ===============")

df_analise_estoque["data_vencimento"] = pd.to_datetime(
    df_analise_estoque["data_vencimento"],
    format="%d/%m/%Y"
)


data_inicial = pd.to_datetime("27/10/2026", format="%d/%m/%Y")
data_final = pd.to_datetime("03/11/2026", format="%d/%m/%Y")

filtro_por_data = df_analise_estoque[
    (df_analise_estoque["data_vencimento"] >= data_inicial) &
    (df_analise_estoque["data_vencimento"] <= data_final)
]

print("\n")
print(filtro_por_data.to_string(index=False))


print("\n\n============== PRODUTOS VENCENDO ESTA SEMANA COM MAIOR QUANTIDADE ===============")


produto_maior_quantidade = filtro_por_data.nlargest(
    1, "quantidade_formatada"
)

print("\n")
print(produto_maior_quantidade.to_string(index=False))


print("\n\n============== COMPRAS RECENTES ===============")


df_analise_estoque["data_compra"] = pd.to_datetime(
    df_analise_estoque["data_compra"],
    format="%d/%m/%Y"
)


data_inicial = pd.to_datetime("24/10/2026", format="%d/%m/%Y")
data_final = pd.to_datetime("27/10/2026", format="%d/%m/%Y")

compra_recente = df_analise_estoque[
    (df_analise_estoque["data_compra"] >= data_inicial) &
    (df_analise_estoque["data_compra"] <= data_final)
]
print("\n")
print(compra_recente.to_string(index=False))



print("\n\n============== PRODUTOS SEM DATA DE VENCIMENTO ===============")


produtos_sem_vencimento = df_analise_estoque[
    df_analise_estoque["data_vencimento"].isna()
]

print("\n")
print(produtos_sem_vencimento.to_string(index=False))



print("\n\n============== INSERINDO COLUNA COM VALOR TOTAL ===============")


valor_total_estoque = (
    df_analise_estoque["preco_formatado"] *
    df_analise_estoque["quantidade_formatada"])


df.insert(9, "valor_total_estoque", valor_total_estoque)
print("\n")
print(df.to_string(index=False))


#print("\n")
#print(df_analise_estoque.to_string(index=False))


print("\n\n============== PRODUTO MAIOR VALOR DE ESTOQUE ===============")


produto_maior_valor = df.nlargest(
    1, "valor_total_estoque"
)

print("\n")
print(produto_maior_valor.to_string(index=False))










