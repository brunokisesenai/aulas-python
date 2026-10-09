# Faça uma requisição HTTP utilizando o requests do python pela API viaCEP:
#
# cep_digitado = input("Digite seu CEP: ")
#
# link = f"https://viacep.com.br/ws/{cep_digitado}/json/"
#
#escrevam os dados de retorno num arquivo historico_pesquisa.json usando o with open()...
# adicionando os valores de pesquisa em uma lista ocntendo todas as pesquisas d CEP feitas pelo usuário.
#Ex: fez 3 pesquisas, o arquivo deverá ter 3 dicionários.



import json

import requests   # Módulo EXTERNO -> Faz requisições HTTP




cep_digitado = input("Digite seu CEP: ")

link = f"https://viacep.com.br/ws/{cep_digitado}/json/"
#link = "https://viacep.com.br/ws/01001000/json/"



resposta = requests.get(link)   #tipos de resposta (200, 300, 400, etc.)

if resposta.status_code == 200:
    print("Requisição feita com sucesso!")
else:
    print("Erro na requisição")


print(resposta.json())

with open("historico_pesquisa.json", "w", encoding="utf-8") as arquivo:
    json.dump(resposta.json(), arquivo, ensure_ascii=False, indent=4)