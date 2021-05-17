##Exercício 6 
#Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média.
##Faça uma aplicação que peça o valor das 3 notas, 
##mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.
'''
def notas(n1, n2, n3):
    n1 = float(input("Digite a nota da prova 1: "))
    n2 = float(input("Digite a nota da prova2: "))
    n3 = float(input("Digite a nota da prova 3: "))
    media3 = (n1 + n2 + n3) / 3
    media2 = n1 + n2 / 2
    media1 = n2 + n3 / 2
    media4 = n1 + n3 / 2
    print ("O valor da média das 3 provas é:" "%.2f" % media3)
    if n1 and n2 > n3:
        print ("A média entre os 2 maiores números é: ", media2)
    elif n1 and n3 > n2: 
        print ("A média entre as 2 maiores notas é: ",media4)
    elif n2 and n3 > n1:
        print ("A média entre as 2 maiores notas é: ",media1)
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    print ("A maior nota é: ", maior, "A menor nota é: ", menor)

    

notas (1,2,3)

'''