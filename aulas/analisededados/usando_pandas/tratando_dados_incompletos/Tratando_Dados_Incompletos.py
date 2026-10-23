import pandas as pd

df_dados_incompletos = pd.DataFrame([
    {
        'nome': 'João de Menezes',
        'cpf': '123.456.789-00'
    },
    {
        'nome': 'Victor Sousa',
        'cpf': '11122233344'
    },
    {
        'nome': 'Marcelo Oliveira',
        'cpf': '333 333 333-99'
    }
])

print(df_dados_incompletos)


df_dados_incompletos.to_csv('dados_incompletos.csv', index=False)

dados = pd.read_csv('dados_incompletos.csv', dtype={'cpf': str})

#print(dados["cpf"])


dados["cpf_formatado"] = (dados["cpf"]
                          .str.replace(".", "")
                          .str.replace("-","")
                          .str.replace(" ", ""))



print(dados)























