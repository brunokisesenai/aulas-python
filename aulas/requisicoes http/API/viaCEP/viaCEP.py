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

with open("dados_cep.json", "w", encoding="utf-8") as arquivo:
    json.dump(resposta.json(), arquivo, ensure_ascii=False, indent=4)












