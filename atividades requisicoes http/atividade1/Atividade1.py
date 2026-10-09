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
import requests

lista_cep = []

while True:
    cep_digitado = input("Digite seu CEP ou 'fim' para finalizar: ")

    if cep_digitado.lower() == "fim":
        break

    link = f"https://viacep.com.br/ws/{cep_digitado}/json/"

    try:
        resposta = requests.get(link)

        endereco = resposta.json()

        # Verifica se o CEP existe
        if "erro" in endereco:
            print("CEP não encontrado!")
            continue

        print(endereco)

        # Adiciona o endereço à lista
        lista_cep.append(endereco)

        # Salva o histórico no arquivo JSON
        with open("historico_pesquisa.json", "w", encoding="utf-8") as arquivo:
            json.dump(
                lista_cep,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

        print("Pesquisa salva no histórico!")

    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição: {erro}")

print("Programa finalizado!")