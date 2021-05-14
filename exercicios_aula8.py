'''Exercícios
1.	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
a.	tamanho da lista.
b.	maior valor da lista.
c.	menor valor da lista.
d.	soma de todos os elementos da lista.
e.	lista em ordem crescente.
f.	lista em ordem decrescente.'''

'''listaL = [5, 7, 2, 9, 4, 1, 3]

tamanho = len(listaL)
maior = max(listaL)
menor = min(listaL)
soma = sum(listaL)
listaL.sort()



print("Tamanho da lista: ", tamanho, "O maior número da lista é: ", maior, "O menor número da lista é: ", menor, "A soma dos elementos da lista é: ", soma, "Lista na ordem crescente: "), 

print("lista em ordem crescente: ", listaL)

listaL.reverse()
print ("lista em ordem decrescente: ", listaL)'''

'''3.	Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
•	"Telefonou para a vítima?"
•	"Esteve no local do crime?"
•	"Mora perto da vítima?"
•	"Devia para a vítima?"
•	"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como 
"Inocente". '''
'''
lista1 = []
lista_perguntas =  ["Telefonou para a vitima?: ", "Esteve no local do crime?: ", "Mora perto da vitima?: ", "Devia para a vítima?",  "Já trabalhou com a vítima?: "]
contador = 0
for lista1 in lista_perguntas:
    resposta = input (lista1)
    if resposta == "sim":
        contador += 1

if contador < 2:
    print ("Inocente")
elif contador == 2:
    print("Suspeito")
elif contador ==3 or contador ==4:
    print ("Cúmplice")

else:
    print ("Assassino")


print(contador)
    '''

