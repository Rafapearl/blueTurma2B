#4.	Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece uma vogal.


vogal = input('Digite uma frase: ').lower()
contador = 0
print (vogal)


for item in vogal :
    if item in "aeiou":
         contador += 1 
print (contador)



