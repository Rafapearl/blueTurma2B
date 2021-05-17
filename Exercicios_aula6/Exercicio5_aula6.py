##5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

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
