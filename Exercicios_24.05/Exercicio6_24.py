#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?"
   # O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

print ("")
print ("=--=" * 30)
print ("                                           JÚRI POPULAR = CRIMES CONTRA A VIDA !!!")
print ("                                                 SISTEMA DE CONTAÇÃO DE VOTOS")

print ("")
print ("By: Rafael Freitas")
print ("=--=" * 30)
print ("")


contador = 0
listaperg = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

for item in listaperg:
    resp = input (item).lower()

    
    if resp == "sim":
       contador += 1
    
if  contador  <2:
    print ("O réu é inocente! ")
elif contador ==2:
    print ('O réu é Suspeito! ')
elif contador ==3 or contador <=4:
    print ("O réu é Cúmplice!")
elif contador == 5:
    print ("O réu é assassino!!!")

print (contador)

