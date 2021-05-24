#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, 
# só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
# onde o computador vai “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos 
# palpites foram necessários para vencer.

print ("")
print ("=--=" * 30)
print ("                                           JOGO: BOLA DE CRISTAL !!!")
print ("")
print ("By: Rafael Freitas")
print ("=--=" * 30)
print ("")

import random
from time import sleep
senha = 3210
digite = int(input("Digite a senha para entrar: "))
numSecreto =   random.randrange(0,21)
contador = 0

while digite != senha:
    print ("Senha incorreta, tente lembrar, você consegue!!!") 
    digite = int(input("Digite a senha para entrar: "))

      


while digite == senha:
    dignum = int(input("Advinhe qual é o número secreto entre 0 e 20: "))
    if dignum == numSecreto:
        sleep (2)
        print (f"Parabéns, você acertou o Número Secreto após {contador} palpite(s)!!!")
        sleep (5)
        break        
    elif dignum > numSecreto:
        sleep (2)
        print ("O número digitado foi MAIOR do que o número secreto! Tente novamente!!! ")
        contador += 1
    elif dignum < numSecreto:
        sleep (2)
        print ("O número digitado foi MENOR do que o número secreto! Tente novamente!!! ")
        contador += 1


    
   