#Filtrem os dados usando o PANDAS do arquivo 'funcionarios.csv' com as seguinte condições:
#todos os salários menores do que 3000, maiores do que 5000 e iguais a 3100
#todos os cargos de Analista de Dados, Analista de Sistemas, Desenvolvedor Java e Cientista de dados
#listar os nomes e cargos d quem tem um salário maior do que 6.000
#listar todos os funcionários com id par


import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=';')
print(df)

print("\n===== TODOS OS SALÁRIOS MENORES DO QUE 3.000, MAIORES DO QUE 5.000 E IGUAIS A 3.100 =====")

print(df[
          (df['salario'] < 3000) |
          (df['salario'] > 5000) |
          (df['salario'] == 3100)
      ])

print("\n\n===== TODOS OS CARGOS DE ANALISTA DE DADOS, ANALISTA DE SISTEMAS, DESENVOLVEDOR JAVA E CIENTISTA DE DADOS =====")

print(df[
          (df['cargo'] == 'Analista de Dados') |
          (df['cargo'] == 'Analista de Sistemas') |
          (df['cargo'] == 'Desenvolvedor Java') |
          (df['cargo'] == 'Cientista de Dados')
      ])

print("\n\n===== NOMES E CARGOS DE QUEM GANHA MAIS DO QUE 6.000 =====")

print(df[
          (df['salario'] > 6000)
      ])

print("\n\n===== FUNCIONÁRIOS COM ID PAR =====")

print(df[
          (df['id'] % 2 == 0)
      ])











