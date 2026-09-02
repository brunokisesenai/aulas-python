#OPERADORES
"""
   ATRIBUIÇÃO
   =  ->  variavel = 10

   !  = NÃO, NOT, CONTRÁRIO...
   SIM -> !SIM = NÃO
   decisao = True
   !decisao = False


   COMPARAÇÃO
   esperar uma resposta de True ou False

   !=  -> se for diferente retorna True; se for igual retorna False
   idade = 18
   idade != 17 -> True
   idade != 18 -> False

   ==  -> se for igual retorna True; se for diferente retorna False

   >  -> se for maior retorna True; se for menor retorna False

   <  -> se for menor retorna True; se for igual retorna False

   >=  -> se for maior e igual retorna True; se for menor e igual retorna False

   <=  -> se for menor e igual retorna True; se for maior retorna False

   PARA MAIS COMPARAÇÕES
   and  -> se todas as comparações forem True, retorna True
   idade = 18
   idade == 18 and idade >18  -> False
     True           False

   or  -> se ao menos uma das comparações for True, retorna True

   not

"""


#TESTES

idade = 18 #INTEIRO
#comparacao = idade !=17 #BOLEANO
#print(comparacao)

#print(idade != 18) #False
#print(idade == 18) #True
#print(idade>19)  #False
#print(idade<19)  #True
#print(idade>=19)  #False
#print(idade<=19)   #True

#print(idade > 10 and idade < 20 and idade == 18) #True
#print(idade == 10 and idade < 20 and idade == 18) #False

#pais_acompanham = True
#print("Na nossa balada não pode entrar crianças, idosos e nem pais de convidados")
#print("Você pode entrar na balada?")
#print((idade >= 18) and (idade < 65) and (pais_acompanham != True))

#pais_acompanham = False
#print("Na nossa balada aceita adulto e criança, Não aceita nem adolescente e nem idoso")
#print("Você pode entrar na balada?")
#print((idade >= 18) and (idade < 65) and (pais_acompanham != True))
#adulto = 18
#idosos = 65
#crianças = entre 0 e 10
#adolescente = entre 11 e 17
#print(idade >= 18 and idade < 65 or idade > 0 and idade <= 10)
