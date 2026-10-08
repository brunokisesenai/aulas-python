import json

# Leitura da base 1
with open("base1.json", "r", encoding="utf-8") as arquivo:
    dados1 = json.load(arquivo)

# Leitura da base 2
with open("base2.json", "r", encoding="utf-8") as arquivo:
    dados2 = json.load(arquivo)

# Leitura da base 3
with open("base3.json", "r", encoding="utf-8") as arquivo:
    dados3 = json.load(arquivo)


# Lista que irá armazenar os aniversariantes
lista_aniversariantes = []


# Processamento da base 1
for funcionario in dados1:
    novo_funcionario = {
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"]
    }

    lista_aniversariantes.append(novo_funcionario)


# Processamento da base 2
for funcionario in dados2:
    novo_funcionario = {
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"]
    }

    lista_aniversariantes.append(novo_funcionario)


# Processamento da base 3
for funcionario in dados3:
    novo_funcionario = {
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"]
    }

    lista_aniversariantes.append(novo_funcionario)


# Ordenação alfabética pelo nome
lista_aniversariantes.sort(key=lambda funcionario: funcionario["nome"])


# Salvando o resultado no arquivo aniversariantes.json
with open("aniversariantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_aniversariantes, arquivo, ensure_ascii=False, indent=4)



# Exibindo o total de registros processados
print(
    f"Total de registros processados com sucesso: "
    f"{len(lista_aniversariantes)}"
)
