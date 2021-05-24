#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

print ("")
print ("=--=" * 30)
print ("                                       MÁQUINA SEPARADORA DE PARES E ÍMPARES!!!")
print ("")
print ("By: Rafael Freitas")
print ("=--=" * 30)
print ("")

dignum = 0
contador = 0
pares = dignum % 2
listpar = []
listimpar = []

while contador != 7:
    dignum = int(input("Digite um número:"))
    if dignum %2 == 0:
        listpar.append (dignum)
    else: 
        listimpar.append (dignum)
    contador += 1


print ("Os valores pares da lista são: ", sorted(listpar)) 
print ("Os valores ímpares da lista são: ", sorted(listimpar))
