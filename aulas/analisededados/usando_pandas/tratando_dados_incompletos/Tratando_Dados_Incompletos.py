import pandas as pd

df_dados_incompletos = pd.DataFrame([
    {
        'nome': 'João de Menezes',
        'cpf': '123.456.789-00',
        'salario': "R$5800"
    },
    {
        'nome': 'Victor Sousa',
        'cpf': '11122233344',
        'salario': "R$7.900,99"
    },
    {
        'nome': 'Marcelo Oliveira',
        'cpf': '333 333 333-99',
        'salario': 1000
    }
])

print(df_dados_incompletos)


df_dados_incompletos.to_csv('dados_incompletos.csv', index=False)

dados = pd.read_csv('dados_incompletos.csv', dtype={'cpf': str})

#print(dados["cpf"])


#dados["cpf_formatado"] = (dados["cpf"]
#                          .str.replace(".", "")
#                          .str.replace("-","")
#                          .str.replace(" ", ""))

#print(dados)

#Transformando CPF ao retirar os símbolos e deixando apenas números
dados["cpf_formatado"] = dados["cpf"].str.replace(r"\D", "", regex=True)


dados["salario_formatado"] = (dados["salario"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r".", "", regex=False)
                              .str.replace(r",", ".", regex=False))

dados["salario_formatado"] = pd.to_numeric(
    dados["salario_formatado"], errors='coerce')


print(dados)

dados["salario_sem_formatação"] = (dados["salario"])



















