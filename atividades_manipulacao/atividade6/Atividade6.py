import json

lista_funcionarios = []


#---------------------------------------------------
#LENDO BASE 1:
#---------------------------------------------------

with open('base1.json', 'r', encoding='utf-8') as arquivo:
    lista_funcionarios = json.load(arquivo)
    linha = []
    for linha in arquivo:
        lista_funcionarios = {
            "nome": linha[0],
            "aniversário": linha[1],
            "cargo": linha[2],
            "salário": float(linha[3]),

        }

        lista_funcionarios.append(linha)


    for linha in arquivo:
        lista_aniversariante = []
        aniversariante = {
            "nome": linha[0],
            "aniversário": linha[1],

        }
        lista_aniversariante.append(aniversariante)


print(f"Lista de Funcionários Base1 {json.dumps(lista_funcionarios, indent=1)}")





#---------------------------------------------------
#LENDO BASE 2:
#---------------------------------------------------

with open('base2.json', 'r', encoding='utf-8') as arquivo:
    lista_funcionarios = json.load(arquivo)
    linha = []
    for linha in arquivo:
        lista_funcionarios = {
            "cargo": linha[0],
            "setor": linha[1],
            "empresa": linha[2],
            "nome": linha[3],
            "aniversário": linha[4],

        }

        lista_funcionarios.append(linha)

    for linha in arquivo:
        lista_aniversariante = []
        aniversariante = {
            "nome": linha[3],
            "aniversário": linha[4],

        }
        lista_aniversariante.append(aniversariante)

print(f"Lista de Funcionários Base 2 {json.dumps(lista_funcionarios, indent=1)}")





#---------------------------------------------------
#LENDO BASE 3:
#---------------------------------------------------

with open('base3.json', 'r', encoding='utf-8') as arquivo:
    lista_funcionarios = json.load(arquivo)
    linha = []
    for linha in arquivo:
        lista_funcionarios = {
            "nome": linha[0],
            "cargo": linha[1],
            "tempo de empresa": linha[3],
            "aniversário": linha[4],

        }

        lista_funcionarios.append(linha)

    for linha in arquivo:
        lista_aniversariante = []
        aniversariante = {
            "nome": linha[0],
            "aniversário": linha[4],

        }
        lista_aniversariante.append(aniversariante)


print(f"Lista de Funcionários Base 3 {json.dumps(lista_funcionarios, indent=1)}")





#---------------------------------------------------
#CRIANDO LISTA DE ANIVERSÁRIO:
#---------------------------------------------------

lista_anversariantes = []

aniversariante = {
    "nome": "",
    "aniversário": "",}

with open("lista_aniversariantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_funcionarios, arquivo, ensure_ascii=False, indent=4)

print(lista_anversariantes)
