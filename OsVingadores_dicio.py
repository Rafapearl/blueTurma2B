''''lista_telefonica = [('Rafael', '11-9-7072.3887'), ('Fernanda', '11-9999.000'), ("Gustavo", '11-8888.0000'), ('Vicente', '11-7777.8888'), ('Luzia', '1111.2222')]
print (lista_telefonica)
print (lista_telefonica[0])
print (lista_telefonica[0][0])

contatos = dict (lista_telefonica)

nome = input("Digite um nome: ")
print (contatos.get(nome, "O nome não foi encontrado!"))'''

vingadores = {'Chris Evans':'Capitão America', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston': 'Loki', 'Chris Hemworth': 'Thor', 'Robert Downey Jr': 'Homem de Ferro', 'Scarlett Johansson':' Viúva Negra'}

personagens = input ("Digite o nome de um personagem: ")
print (vingadores.get (personagens, "O nome não foi encontrado!"))

vingadores ["Jason"] = "Terror das águas"
vingadores ["Freddie"] = "Mestre dos Pesadelos!"
vingadores ["O mascara"] = "Arrasando corações"
vingadores ["Viuva Negra"] = "invencivel"
vingadores ["Rafael"] = "Eu"
#Deletando Valores
del vingadores ["Rafael"]
print (vingadores)

excluido_pop = vingadores.pop('Mark Ruffalo', 'nome não encontrado')
print (excluido_pop)

excluidospop = vingadores.popitem()
print (excluidospop)