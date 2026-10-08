dicionario_frutas = {
    "frutas": [
        {
            "nome": "maçã",
            "tipo": ["gala", "importada"]
        },
        {
            "nome": "banana",
            "tipo": ["prata", "nanica", "maçã", "da terra"]
        }
    ]
}


for produto in dicionario_frutas["frutas"]:
    print(f"Produto:", produto["nome"])
    for tipo in produto["tipo"]:
        print(f"Tipo: {tipo}")
