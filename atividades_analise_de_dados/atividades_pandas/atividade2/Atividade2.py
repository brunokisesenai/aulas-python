#Depois de completar a atividade 1... crie um arquivo 'cargos_altos.csv' que armazene uma base de dados nova.
#Os dados slavos nesse novo arquivo deverão ser lidos do 'funcionarios.csv' com um filtro de funcionários com salário acima de 6000
#Adicioname mais 5 funcionários com id, nome, salario e cargos novos
#Apague os 2 primeiros funcinoários com idex de 0 e 1 do arquivo
#Adicione mais uma coluna na tabela com o nome de 'tempo_empresa' para armazenar em meses (int) o tempo que o funcionário está na empresa

import pandas as pd

print("=============== CRIANDO ARQUIVO 'CARGOS_ALTOS.CSV' ================")

# Criar um DataFrame vazio com as colunas
df = pd.DataFrame(columns=["id", "Nome", "Salario", "Cargo"])

# Salvar como arquivo CSV
df.to_csv("cargos_altos.csv", index=False, sep=",", encoding="utf-8")

print("Arquivo 'cargos_altos.csv' criado com sucesso!")


print("\n\n=============== CRIANDO ARQUIVO 'CARGOS_ALTOS.CSV' ================")

df = pd.read_csv("funcionarios.csv",sep=";")
df = df.rename(columns={
    'id': "identificador",
    "nome": "funcionario"
})
# print(df[['funcionario', 'identificador']])
novo_funcionario = [
    {
        'identificador': 31,
        'funcionario': "João de Menezes",
        'salario': 100000.0,
        'cargo': "Instrutor SENAI"
    }
]

novo_funcionario = pd.DataFrame(novo_funcionario)
mais_um_funcionario = pd.DataFrame([{
    'identificador': 32,
    'funcionario': "Victor Sousa",
    'salario': 1000.0,
    'cargo': "Interpret SENAI"
}])

df = pd.concat([df, novo_funcionario, mais_um_funcionario], ignore_index=True)
df = df.drop(df[df['identificador'] == 31].index)

df.loc[df['identificador'] == 2, ["funcionario"]] = ["Bruno da Silva"]
df.loc[df['identificador'] == 1, ["funcionario", "salario", "cargo"]] = [
    "Ana Maria",10000.00, "CEO"
]
print(df)
df.to_csv("funcionarios.csv",sep=";",index=False)




















