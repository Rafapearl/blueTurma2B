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