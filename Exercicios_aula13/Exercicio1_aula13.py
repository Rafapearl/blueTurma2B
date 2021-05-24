#Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
#celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
#retornar a data completa. Não esqueça de validar se a celebridade escolhida está
#presente em seu dicionário.

aniversario = dict()

while True:
    nome = input ('Digite um nome de uma celebridade ou 0 para sair:')
    if nome == 0: break
    data = input ("Digite a data de nascimento da celebridade (dd/mm/yyyy)")
