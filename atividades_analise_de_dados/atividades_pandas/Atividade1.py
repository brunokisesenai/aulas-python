#Filtrem os dados usando o PANDAS do arquivo 'funcionarios.csv' com as seguinte condições:
#todos os salários menores do que 3000, maiores do que 5000 e iguais a 3100
#todos os cargos de Analista de Dados, Analista de Sistemas, Desenvolvedor Java e Cientista de dados
#listar os nomes e cargos d quem tem um salário maior do que 6.000
#listar todos os funcionários com id par


import pandas as pd

df = pd.read_csv("dados_da_lista.csv")
print(df)