# IMPORTANDO BIBLIOTECA, PACOTE, MÓDULO
# import -> nome da biblioteca
# como a biblioteca json é nativa do Python, nós não precisamos intalar ela no projeto
import json # JSON -> JavaScript Object Notation

dados_dicionario = [
    {
        'produto': 'Frango',
        'preco': 20.00,
        'em_estoque': True
    },
    {
        'produto': 'Carne',
        'preco': 45.00,
        'em_estoque': True
    },
    {
        'produto': 'Arroz',
        'preco': 16.00,
        'em_estoque': True
    }
]

# escreve um documento json
# dump -> transforma um dicionário em json
with open('json_file.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_dicionario, arquivo, ensure_ascii=True, indent=4)
    print("Arquivo escrito\n")

# lê o documento json
# .load -> transforma o arquivo JSON em dicionário python
with open('json_file.json', 'r', encoding='utf-8') as arquivo:
    novo_dicionario = json.load(arquivo)

# with open('json_file.json', 'a', encoding='utf-8') as arquivo:
#     texto_adicinoal = json.dumps('[{"produto": "Arroz","preco": 50, "em_estoque": true}]', ensure_ascii=False, indent=1)
#     novo_obj = json.loads(texto_adicinoal)
#
#     json.dump(novo_obj, arquivo, ensure_ascii=False, indent=1)
#     print("Arquivo adicionado\n")

# dumps -> transforma o texto python em arquivo json
for produto in novo_dicionario:
    print(f'Dicionário: {produto}')
    print(f"Arquivo JSON {json.dumps(produto, indent=1)}")

    print(produto['preco'])