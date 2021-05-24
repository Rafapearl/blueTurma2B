#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada 
# pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

print ("")
print ("=--=" * 30)
print ("                                           MEGA CONTADORA E REMOVEDORA DE VOGAIS !!!")
print ("")
print ("By: Rafael Freitas")
print ("=--=" * 30)
print ("")

frase = input ("Digite uma frase: ").lower()
vogais = 0

for item in frase:
    if item in "aeiou":
        vogais += 1
print (f"A sua frase possui {vogais} vogais")
print ('A sua frase sem vogais: ', frase.replace('a','').replace('e', ''). replace('i', ''). replace('o', '').replace('u',''))