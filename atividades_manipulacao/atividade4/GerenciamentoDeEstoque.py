import json

dicionario_loja = {
    'nome': 'TechStore',
    'produtos': ['nome', 'preco', 'quantidade'],
}

dados_produtos = [
    {
        'nome': 'Frango',
        'preco': 20.00,
        'quantidade': 10
    },
    {
        'nome': 'Carne',
        'preco': 45.00,
        'quantidade': 30
    },
    {
        'nome': 'Arroz',
        'preco': 16.00,
        'quantidade': 20
    }
]



with open('estoque.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_produtos, arquivo, ensure_ascii=True, indent=4)
    print("LISTA DE PRODUTOS DA LOJA TECHSTORE!\n")

with open('estoque.json', 'r', encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)


for produto in dados_produtos:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")


dados_produtos.append(
  {
    'nome': 'Sushi',
    'preco': 100.00,
    'quantidade': 15
  }
)


with open('estoque.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_produtos, arquivo, ensure_ascii=True, indent=4)
    print("\n\nLISTA DE PRODUTOS DA LOJA TECHSTORE ATUALIZADA!\n")

with open('estoque.json', 'r', encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)


for produto in dados_produtos:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")