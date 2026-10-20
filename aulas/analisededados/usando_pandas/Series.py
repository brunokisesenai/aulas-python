import pandas as pd


#VERIFICARR VERSÃO PANDAS
#print(pandas.__version__)

#SERIES
# Uma dimensão -> Vetor
nomes = ["João", "Felipe", "André"]

#print(nomes) #lista
#print("\n\n")

indexes = ["pessoa1", "pessoa2", "pessoa3"]
nomes_series = pd.Series(nomes, index= indexes)
#print(nomes_series) #series do pandas
coluna_idades = pd.Series([25, 30, 35, 40, 45], index= ["a", "b", "c", "d", "e"])
#print(coluna_idades[coluna_idades < 30])    #retorna uma linha
#print(coluna_idades.loc['a'])               #retorna o valor



#DATAFRAMES
# valores com várias dimensões -> Matriz

notas = {
    "nome": ["Italo", "Bruno", "Charlie", "Maikon"],
    "turma": ["Python", "Java", "Banco de Dados", "Front-end"],
    "notas": [10, 8, 5 , 6]
}


#adiciona os nomes para index
df = pd.DataFrame(notas, index= ["aluno1", "aluno2", "aluno3", "aluno4"])

print("===== PRMEIRA LISTA =====")
print(df)
#print(df.loc["aluno1"])   #procura pela chave
#print(df.iloc[1])          #procura pelo index

print("\n\n===== LISTA ATUALIZADA =====")

#CRIA NOVA COLUNA
df["status"] = ["Aprovado", "Aprovado", "Reprovado", "Reprovado"]
print(df)
#print(df.loc["aluno1"])
#print(df.iloc[1])

nova_linha = pd.DataFrame([{
    "nome": "Victor",
    "turma": "Python",
    "notas": 9,
    "status": "Aprovado",
},
{
    "nome": "Nael",
    "turma": "Javascript",
    "notas": 2,
    "status": "Reprovado",
}
], index= ["aluno5", "aluno6"])

df = pd.concat([df, nova_linha])

print("\n\n===== LISTA ATUALIZADA - NOVA LINHA=====")
print(df)


print("\n\n===== LISTA ALUNOS PYTHON =====")

filtro = df[df["turma"] == "Python"]

print(filtro)


print("\n\n===== LISTA ALUNOS APROVADOS =====")

filtro1 = df[df["status"] == "Aprovado"]

print(filtro1)


print("\n\n===== LISTA NOME E TURMA =====")

for indice in df.index:
    print(f"{indice} - Nome: {df.loc[indice, 'nome']} | Turma: {df.loc[indice, 'turma']}")


print("\n\n\n")
filtro = df[['nome', 'status']]
print(filtro)













