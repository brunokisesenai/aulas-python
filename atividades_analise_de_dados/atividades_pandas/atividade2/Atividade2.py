#Depois de completar a atividade 1... crie um arquivo 'cargos_altos.csv' que armazene uma base de dados nova.
#Os dados sALvos nesse novo arquivo deverão ser lidos do 'funcionarios.csv' com um filtro de funcionários com salário acima de 6000
#Adicioname mais 5 funcionários com id, nome, salario e cargos novos
#Apague os 2 primeiros funcinoários com idex de 0 e 1 do arquivo
#Adicione mais uma coluna na tabela com o nome de 'tempo_empresa' para armazenar em meses (int) o tempo que o funcionário está na empresa

import pandas as pd

print("=============== CRIANDO ARQUIVO 'CARGOS_ALTOS.CSV' ================")

# Criar um DataFrame vazio com as colunas
df = pd.read_csv("funcionarios.csv",sep=";")

# Salvar como arquivo CSV
df.to_csv("cargos_altos.csv", index=False, sep=",", encoding="utf-8")

print("\nArquivo 'cargos_altos.csv' criado com sucesso!")


print("\n\n=============== CRIANDO 'CARGOS_ALTOS.CSV' COM SALÁRIOS ACIMA DE 6.000 ================")

salario_alto = df[
    df['salario'] > 6000
]

print(salario_alto)


salario_alto.to_csv('cargos_altos.csv', index=False, encoding='utf-8', sep=";")
df_filtrado = pd.read_csv("cargos_altos.csv", sep=";")
print(df_filtrado)





print("\n\n=============== ADICIONANDO 05 FUNCIONÁRIOS NOVOS ================")

df = pd.read_csv("cargos_altos.csv",sep=";")


funcionario31 = pd.DataFrame([{
    'identificador': 31,
    'funcionario': "Daniel Matos",
    'salario': 1000.0,
    'cargo': "Programador Python"
}])

funcionario32 = pd.DataFrame([{
    'identificador': 32,
    'funcionario': "Mikhail Oliveira",
    'salario': 7000.0,
    'cargo': "Bancário"
}])

funcionario33 = pd.DataFrame([{
    'identificador': 33,
    'funcionario': "Alan Alvetti",
    'salario': 50000.0,
    'cargo': "Desenvolvedor Web"
}])

funcionario34 = pd.DataFrame([{
    'identificador': 34,
    'funcionario': "Talya Vogado",
    'salario': 100000.0,
    'cargo': "Publicitária"
}])

funcionario35 = pd.DataFrame([{
    'identificador': 35,
    'funcionario': "Bruno Kise",
    'salario': 15000.0,
    'cargo': "Desenvolvedor Python"
}])


df = pd.concat([df, funcionario31, funcionario32, funcionario33, funcionario34, funcionario35], ignore_index=True)
df.to_csv("cargos_altos.csv",index=False)


print("\nFuncionários adicionados com sucesso!")


print("\n\n=============== REMOVENDO DOIS FUNCIONÁRIOS DO ARQUIVO 'FUNCIONARIOS.CSV' ================")

df = pd.read_csv("funcionarios.csv",sep=";")

df = df.drop(df[df['identificador'] == 0].index)
df = df.drop(df[df['identificador'] == 1].index)

df.to_csv("funcionarios.csv",sep=";",index=False)

print("\nFuncionários removidos!")

print("\n\n=============== ADICIONANDO NOVA COLUNA ================")

df = pd.read_csv("cargos_altos.csv",sep=";")

df['Tempo de Empresa'] = [10,10,12,13,14,15,16,17,18,20]

print(df)

#nova_lista = ['Tempo de Empresa']

#df['Tempo de Empresa'] = nova_lista



df.to_csv('cargos_altos.csv', index=False, encoding='utf-8', sep=";")










