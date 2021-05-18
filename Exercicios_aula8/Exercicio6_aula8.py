#6.	Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.


frase = input("Digite uma frase: ").lower().replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print (frase)