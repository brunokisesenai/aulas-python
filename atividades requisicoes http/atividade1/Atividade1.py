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


lista_cep = []

while True:

    cep_digitado = input("Digite seu CEP ou 'fim para finalizar: ")
    if cep_digitado != "fim":
        link = f"https://viacep.com.br/ws/{cep_digitado}/json/"




        resposta = requests.get(link)   #tipos de resposta (200, 300, 400, etc.)

        print(resposta.json())


        for endereco in lista_cep:
            endereco  = {
                "cep": endereco['cep'],
                "logradouro": endereco['logradouro'],
                "complemento": endereco['complemento'],
                "unidade": endereco['unidade'],
                "bairro": endereco['bairro'],
                "localidade": endereco['localidade'],
                "uf": endereco['uf'],
                "estado": endereco['estado'],
                "regiao": endereco['regiao'],
                "ibge": endereco['ibge'],
                "gia": endereco['gia'],
                "ddd": endereco['ddd'],
                "siafi": endereco['siafi'],
            }

            lista_cep.append(endereco)


    else:
        break

with open("historico_pesquisa.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_cep, arquivo, ensure_ascii=False, indent=4)