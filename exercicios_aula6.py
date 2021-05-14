## 1.	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

'''def soma4(x1, y1, z1):
    soma = x1 + y1 + z1
    print (f"valor da soma é: {soma}")
      
a=  int(input("Digite um número a ser somado"))
b=  int(input("Digite um número a ser somado"))
c=  int(input("Digite um número a ser somado"))
soma4 (a, b, c)'''

## 2 - Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 
# ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

'''def posinega(x=0):
    x = int(input("Digite aqui o valor desajado: "))
    if x >0:
        print("P")
    elif x<0:
        print("N")
    elif x==0:
        print("0")


posinega(0)'''

## 3 = eFaça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de 
# imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
  
'''def somaImposto(taxaImposto, custo):
    taxaImposto_float = float(taxaImposto)/100
    custo_reajustado = custo + (custo * taxaImposto_float)
    print(f'O valor do custo com taxa do imposto é {custo_reajustado:.2f}')

custo = float(input("Valor do Produto = R$ "))
taxaImposto = input("Taxa do imposto = ").replace("%","")
somaImposto(taxaImposto, custo)'''


##4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
''''
def salariocheio():
    salario = int(input("Digite aqui o seu salário por hora: "))
    horas = int(input("Digite aqui quantas horas você trabalha"))
    salariotodo = (salario * 1,5)
    if horas > 40:
        print (salariotodo)
    return salariotodo

salariocheio()'''

##5. 5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

'''def IMC(altura,peso):
    imc_calculado = peso /(altura ** 2)
    if imc_calculado < 18.5:
        print("Magreza")
    elif imc_calculado >= 18.5 and imc_calculado < 24.9:
        print("Normal")
    elif imc_calculado >= 24.9 and imc_calculado <= 30:
        print("Sobrepeso")
    else:
        print("Obesidade")

str_altura = float((((input("Digite sua altura em metros: ").replace(',','.')).lower()).replace('m',' ')).strip())
str_peso = float((((input("Digite seu peso: ").replace(',','.')).lower()).replace('kg',' ')).strip())
IMC(str_altura,str_peso)
print("Resultado: ")
IMC(1.68,75)'''

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

## 7.7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

'''def menornumero (x1, y1):
    x1 = int(input("Digite um número aqui: "))
    y1 = int(input("Digite outro número aqui: "))
    if x1 < y1:
        print (x1)
    elif y1< x1:
        print (y1)
    elif y1==x1:
        print ("Números iguais")

menornumero (x1=3, y1=1)'''

##DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.
'''
def dataImpressa(data):  
    dia = int(data[:2])
    mes = data[3:5]
    ano = int(data[6:])
    if mes > "12" or mes == "00":
        print("Data Inválida!")
    if mes == "01":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Janeiro de {ano}.")
    elif mes == "03":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Março de {ano}.")
    elif mes == "05":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Maio de {ano}.")
    elif mes == "07":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Julho de {ano}.")
    elif mes == "08":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Agosto de {ano}.")
    elif mes == "10":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Outubro de {ano}.")
    elif mes == "12":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Dezembro de {ano}.")
    elif mes == "04":
        if dia > 30:
                print("Data Inválida!")
        else:
            print (f"{dia} de Abril de {ano}.")
    elif mes == "06":
        if dia > 30:
                print("Data Inválida!")
        else:
                print (f"{dia} de Junho de {ano}.")
    elif mes == "09":
        if dia > 30:
                print("Data Inválida!")
        else:
                print (f"{dia} de Setembro de {ano}.")
    elif mes == "11":
        if dia > 30:
                print("Data Inválida!")
        else:
                print (f"{dia} de Novembro de {ano}.")

    elif mes == "02": 
        if (ano % 4 == 0 or ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                print("Data Inválida!")
            else:
                print (f"{dia} de Fevereiro de {ano}.")
        if (ano % 4 != 0 or ano % 100 == 0) or ano % 400 != 0:
            if dia > 28:
                print("Data Inválida!")
            else:
                print (f"{dia} de Fevereiro de {ano}.")
            
  
data = input("Digite uma data (Formato DD/MM/AAA): ")

dataImpressa(data)
'''
