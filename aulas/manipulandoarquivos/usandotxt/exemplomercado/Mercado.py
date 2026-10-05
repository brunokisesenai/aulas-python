produtos = []

produtos.append("Leite")
produtos.append("Macarrão")
produtos.append("Carne")
produtos.append("Açaí")






#for produto in produtos:
#   print(produto)


#ESCRITA  ->  Write  ->  w
#open  ->  cria/usa 'arquivo.txt'
#as  ->  cria variável arquivo e atribui os valores do documento arquivo.txt à ela

#with open("recibo.txt", "w", encoding="utf-8") as arquivo:
#    for produto in produtos:
#        arquivo.write(f"{produto}\n")



#LEITURA  ->  read  -> r
#open  ->  ler todos os textos escritos dentro do recibo.txt
with open("recibo.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

    posicao = texto.find("Iogurte")

    print(posicao)

    produto_vencido = texto[posicao:posicao+7]

    print(f"O produto {produto_vencido} está vencido.")





