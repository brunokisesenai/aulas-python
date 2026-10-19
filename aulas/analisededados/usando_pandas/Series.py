import pandas as pd


#VERIFICARR VERSÃO PANDAS
#print(pandas.__version__)

#SERIES
nomes = ["João", "Felipe", "André"]

#print(nomes) #lista
#print("\n\n")

indexes = ["pessoa1", "pessoa2", "pessoa3"]
nomes_series = pd.Series(nomes, index= indexes)
#print(nomes_series) #series do pandas
coluna_idades = pd.Series([25, 30, 35, 40, 45], index= ["a", "b", "c", "d", "e"])
print(coluna_idades[coluna_idades < 30])    #retorna uma linha
print(coluna_idades.loc['a'])               #retorna o valor







#DATAFRAMES









