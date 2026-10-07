
import json

# ETAPA 1 - LENDO O ARQUIVO TXT

catalogo_livros = []

with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip().split(';')

        if linha:

            livro = {
                "id": int(linha[0]),
                "nome": linha[1],
                "descricao": linha[2],
                "preco": float(linha[3]),
                "em_estoque": int(linha[4])
            }

            catalogo_livros.append(livro)



# ETAPA 2 - GERANDO O ARQUIVO JSON


with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, ensure_ascii=False, indent=4)



# ETAPA 3 - ADICIONANDO 5 NOVOS LIVROS


livro31 = {
    "id": 31,
    "nome": "O Guia do Mochileiro das Galaxias",
    "descricao": "Comedia de ficcao cientifica e aventuras espaciais",
    "preco": 39.90,
    "em_estoque": 12
}

livro32 = {
    "id": 32,
    "nome": "Dracula",
    "descricao": "Classico de terror sobre o famoso vampiro",
    "preco": 45.00,
    "em_estoque": 9
}

livro33 = {
    "id": 33,
    "nome": "It: A Coisa",
    "descricao": "Terror sobre uma entidade sobrenatural",
    "preco": 59.90,
    "em_estoque": 6
}

livro34 = {
    "id": 34,
    "nome": "O Diario de Anne Frank",
    "descricao": "Relato de uma jovem durante a Segunda Guerra Mundial",
    "preco": 35.00,
    "em_estoque": 20
}

livro35 = {
    "id": 35,
    "nome": "Sherlock Holmes",
    "descricao": "Historias de misterio do famoso detetive",
    "preco": 42.50,
    "em_estoque": 14
}

# Adicionando os novos livros à lista principal
catalogo_livros.append(livro31)
catalogo_livros.append(livro32)
catalogo_livros.append(livro33)
catalogo_livros.append(livro34)
catalogo_livros.append(livro35)


# Atualizando o mesmo arquivo catalogo.json
with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, ensure_ascii=False, indent=4)



# ETAPA 4 - LENDO OS DADOS DO ARQUIVO JSON


with open("catalogo.json", "r", encoding="utf-8") as arquivo:
    catalogo = json.load(arquivo)



# Livros com menos de 15 unidades em estoque


print("=====LIVROS COM MENOS DE 15 UNIDADES EM ESTOQUE:=====")
print(f"\n")

for livro in catalogo:
    if livro["em_estoque"] < 15:
        print(
            f'{livro["nome"]} - '
            f'{livro["em_estoque"]} unidades'
        )



# Valor total do estoque

valor_total_estoque = 0

for livro in catalogo:
    valor_total_estoque += livro["preco"] * livro["em_estoque"]


print()
print("-" * 50)
print(f"VALOR TOTAL DO ESTOQUE: R$ {valor_total_estoque:.2f}")

