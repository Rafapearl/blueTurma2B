#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.


def conta_vogais(frase):
    vogais = 0

    for item in frase:
        if item in "aeiou":
            vogais += 1
    print (f"A sua frase possui {vogais} vogais")
    print ('A sua frase sem vogais: ', frase.replace('a','').replace('e', ''). replace('i', ''). replace('o', '').replace('u',''))

frase = input ("Digite uma frase: ").lower()

conta_vogais(frase)
