#IMPORTANDO BIBLIOTECA, PACOTE, MÓDULO
#import -> nome da biblioteca
#como a biblioteca json é nativo do Python, nós não precisamos instalar a biblioteca

import json

dados_dicionario = {
    'produto': 'frango',
    'preço': 20.00,
    'em_estoque': True
}

json_string = json.dumps(dados_dicionario)
print(json_string)