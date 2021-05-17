## 6.Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).
'''
def nota_aluno():
    notaluno = float(input("Digite a nota do aluno: "))
    if notaluno <= 5.9:
        print ("nota F")
    elif notaluno >=6.0 and notaluno <=6.9:
        rint ("nota D")
    elif notaluno >=7.0 and notaluno <8.0:
        print ("nota C")
    elif notaluno >=8.0 and notaluno <9.0:
        print ("nota B")
    elif notaluno >= 9.0 and notaluno <=10:
        print ("Parabéns!!! nota A")
    else:
        print ("valor inválido")

nota_aluno()'''