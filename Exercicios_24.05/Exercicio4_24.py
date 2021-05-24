#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Valide a data e retorne NULL caso a data seja inválida.
def data_extenso():
    
    print ("")
    print ("=--=" * 30)
    print ("                                           CONVERSOR: DATA POR EXTENSO !!!")
    print ("")
    print ("By: Rafael Freitas")
    print ("=--=" * 30)
    print ("")

    
    print ("Digite uma data no formato DD/MM/YYYY!" )
    digdia = input("Comece digitando o dia: ")
    digmes = input ("Digite o mês: ")
    digano = input ("Digite o ano: ")


    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']


    if digmes == "1" or digmes == "01":
        print (f'Você digitou o dia {digdia} de {mes[0]} de {digano}')
    elif digmes == "2"  or digmes == "02":
        print (f'Você digitou o dia {digdia} de {mes[1]} de {digano}')
    elif digmes == "3"  or digmes == "03":
        print (f'Você digitou o dia {digdia} de {mes[2]} de {digano}')
    elif digmes == "4" or digmes == "04":
        print (f'Você digitou o dia {digdia} de {mes[3]} de {digano}')
    elif digmes == "5" or digmes == "05":
        print (f'Você digitou o dia {digdia} de {mes[4]} de {digano}')
    elif digmes == "6"  or digmes == "06":
        print (f'Você digitou o dia {digdia} de {mes[5]} de {digano}')
    elif digmes == "7" or digmes == "07":
        print (f'Você digitou o dia {digdia} de {mes[6]} de {digano}')
    elif digmes == "8" or digmes == "08":
        print (f'Você digitou o dia {digdia} de {mes[7]} de {digano}')
    elif digmes == "9" or digmes == "09":
        print (f'Você digitou o dia {digdia} de {mes[8]} de {digano}')
    elif digmes == "10":
        print (f'Você digitou o dia {digdia} de {mes[9]} de {digano}')
    elif digmes == "11":
        print (f'Você digitou o dia {digdia} de {mes[10]} de {digano}')
    elif digmes == "12":
        print (f'Você digitou o dia {digdia} de {mes[11]} de {digano}')
    else: 
        print( "Digite uma data válida! ")


data_extenso()