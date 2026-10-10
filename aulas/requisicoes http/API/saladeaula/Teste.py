import json
import requests

link = 'http://192.168.205.100:8080/usuarios'
link_cep = 'http://viacep.com.br/ws/01001000/json/'

#REQUISIÇÕES GET
resposta = requests.get(link)

print(f"STATUS BUSCA DADOS: {resposta}")   # 200
print(resposta.json())   # mostra as informações no terminal


# chaves aceitas na API  da aula: 'nome', 'email'

meus_dados = {
    'nome': 'Bruno',
    'email': 'bruno.kise@aluno.senai.br',

}


#REQUISIÇÕES POST
envio = requests.post(link, json=meus_dados)
print(f"STATUS ENVIO DE DADOS: {envio}")
print(envio.json())


resposta = requests.get(link+"/1")
print(f"BUSCA DE DADOS POR ID: {resposta}")


# REQUISIÇÃO PUT   ->>  atualiza informações existentes na base de dados
dado_atualizado = {
    "nome": "Bruno",
    "email": "bruno.kise@aluno.senai.br",

}

atualizacao = requests.put(link+"/1", json=dado_atualizado)

#REQUISIÇÕES DELETE

deletar = requests.delete(link+"/1")
print(f"STATUS DELETAR: {deletar}")

while True:
    novo_dado = {
        "nome": "NOME ALEATÓRIO",
        "email": "EMAIL ALEATÓRIO"
    }

    #enviando_dados_aleatorios = requests.post(link, json=novo_dado)
    #print(enviando_dados_aleatorios)   --->>> VAI LANÇAR VÁRIOS USUÁRIOS INFINITAMENTE


#FAZENDO BUSCAS E SALVANDO NA MINHA BASE DE DADOS

    busca_cep = requests.get(link_cep)
    busca_pessoa = requests.get(link+'/1')

    lista_pessoas = []

    lista_pessoas.append(busca_pessoa.json())
    lista_pessoas.append(busca_cep.json())

    print(lista_pessoas)

    print(f"nome da pessoa: {lista_pessoas[0]['nome']}\n"
          f"CEP da pessoa: {lista_pessoas[1]['cep']}\n")

    with open("pessoas.json", "w", encoding='utf-8') as arquivo:
        json.dump(lista_pessoas, arquivo, indent=4, ensure_ascii=False)











