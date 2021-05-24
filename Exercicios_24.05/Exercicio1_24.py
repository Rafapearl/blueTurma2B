#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:

   # A soma deles;

   # A multiplicação entre eles;

   # A divisão inteira deles;

   # Mostre na tela qual é o maior;

   # Verifique se o resultado da soma é par ou impar e mostre na tela;

   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

print ("")
print ("=--=" * 30)
print ("                                        BEM-VINDO A CALCULADORA ESPECIAL!!!")
print ("")
print ("By: Rafael Freitas")
print ("=--=" * 30)
print ("")


num1 = int(input("Insira o número 1: "))
num2 = int(input("Insira o número 2: "))

soma = num1 + num2
multi = num1 * num2
divi = num1 // num2
print ("O valor da soma entre os dois números é:", soma)
print ("O valor da multiplicação entre os dois números é:", multi)
print ("O valor da divisão entre os dois números é:", divi)

if num1 > num2:
    print ("O primeiro número digitado é o maior!")
elif num2 > num2:
    print ("O segundo número digitado é o maior!")
else: 
    print ("Os números são iguais!!")

if soma%2 ==1:
    print ("A soma entre os dois números é ímpar")
else:
    print ("A soma entre os dois números é par!")

if multi > 40:
    multi
    multi_divi = multi // divi
    print ("A divisão entre o resultado multiplcado é:", multi_divi)
else:
    print ("A multiplicação entre os números não é maior que 40!! ")


print ("")
print ("=--=" * 30)
print ("                                                 TESTE UM NOVO NÚMERO !!!")
print ("=--=" * 30)
print ("")
