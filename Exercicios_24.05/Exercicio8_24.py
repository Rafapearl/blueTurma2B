#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , 
# além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

print ("")
print ("=--=" * 30)
print ("                                       SIMULE O TEMPO DE SUA APOSENTADORIA !!!")
print ("")
print ("By: Rafael Freitas")
print ("=--=" * 30)
print ("")

nomedig = input ("Digite o seu nome: ")
anodig = int(input("Digite o ano de seu nascimento: "))
digctps = int(input("Digite o número da sua carteira de trabalho ou '0' caso não possua: "))


datanasc = (anodig - 2021) * -1

dicio = {nomedig: [anodig, digctps, datanasc, 'Sem carteira de trabalho']}

baseaposenta = 1986

if digctps != 0:
    anocon = int(input("Qual foi o ano da sua contratação?: "))
    salario = float(input("Qual é o seu salário? "))
    temporestante = baseaposenta  - anocon 
    temporestantepos = temporestante * -1
    restanteidade = datanasc + (temporestante * -1)
    dicio [nomedig] [3]= [anocon, salario, temporestantepos, restanteidade]
    print (f"{nomedig}, nascido no ano {anodig}, com {datanasc} de idade, com a carteira de trabalho n. {digctps}, contratado no ano {anocon}, com o salário de R$ {salario}, rentando {temporestantepos} anos para se aposentar, quando terá {restanteidade} anos de idade!")
else:
    semcarteira = "(Resta a carterira de Trabalho para demais informações)"
    print (f"{nomedig}, nascido no ano {anodig}, com {datanasc} de idade, {semcarteira}")


          

print (dicio)

