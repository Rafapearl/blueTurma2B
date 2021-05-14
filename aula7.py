##Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. Se eles forem iguais, 
#imprima que são valores idênticos.
"""
def new_func(x1, y1):
    if x< y:
         print(x)
    elif x> y: 
        print(y)
    elif x==y:
        print("números iguais")
"""

        
##Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) 
#como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

'''
def numeros ():
    from random import randint
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um valor: "))
    soma1 = n1 + n2 
    limite = randint(1,100)

    print (limite)
    if soma1 > limite:
        print ("O valor da soma é maior do que o limite aleatório!!")
    else:
        print ("O valor é menor do que  o limite aleatório!!")
   
numeros()
'''

""""
def maior_soma(a, b, l):
    if n1 + n2 > limite:
        print('A soma entre {} e {} é maior que o limite!'.format(n1,n2))
    else:
        print('A soma entre {} e {} não é maior que o limite!'.format(n1,n2))
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
limite = int(input('Digite o limite:'))
maior_soma(n1, n2, limite)"""

###Exercício Treino 3 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. 
# Faça uma chamada à função, passando como parâmetro uma string.
"""
"""
"""def string(a = str):
    digite = input("Digite uma palavra: ").upper()
    print (digite)
    return digite

string()
"""
"""
def min(string):
    return string.upper()
string = str(input('Digite uma frase:'))
print(min(string))
"""

##Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa 
# tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.
'''
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <16:
        return f'Com {idade} anos VOTO:NEGADO'
    elif idade >=16 and idade <18:
        return f'Com {idade} anos VOTO:OPCIONAL'
    else:
        return f'Com {idade} anos VOTO:OBRIGATORIO'

nasc = int(input('Em que ano você nasceu:'))
print(voto(nasc))'''



## Exercício 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e
#  quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido 
# informado corretamente.
'''
def ficha(j, g):
    j = (input("Digite o nome de um jogador de futebol: ")).capitalize()
    g = int(input("Digite quantos gols o jogador marcou: "))
    print (f"O jogador {j} marcou {g} na história do futebol!")
  
ficha(0,1)

'''


##Exercício 6 
#Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média.
##Faça uma aplicação que peça o valor das 3 notas, 
##mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

def notas(n1, n2, n3):
    n1 = float(input("Digite a nota da prova 1: "))
    n2 = float(input("Digite a nota da prova2: "))
    n3 = float(input("Digite a nota da prova 3: "))
    media3 = n1 + n2 + n3 / 3
    media2 = n1 + n2 / 2
    media1 = n2 + n3 / 2
    media4 = n1 + n3 / 2
    print ("%.2f" % media3)
    if n1 and n2 > n3:
        print (media2)
    elif n1 and n3 > n2: 
        print (media4)
    elif n2 and n3 > n1:
        print (media1)
    
    

notas (1,2,3)

