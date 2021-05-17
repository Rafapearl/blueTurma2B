###PROJETO: Gastos com viagem -  Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, 
# aluguel de carro e gastos extras de uma viagem para uma determinada cidade.


#H0SPEDAGEM
#1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, 
#sendo que 1 noite custa R$ 140,00.


def custo_hotel(noites):
    noites = noites * 140
    return (noites)

    





#Passagem

#2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
#- São Paulo custa R$ 312,00;
#- Porto Alegre custa R$ 447,00;
#- Recife custa R$ 831,00;
#- Manaus custa R$ 986,00."""

def custo_aviao(cidade):
    if cidade  == 'SÃO PAULO':
        custo_da_passagem = 312.00
        return custo_da_passagem
    elif cidade == 'PORTO ALEGRE':
        custo_da_passagem = 447.00
        return custo_da_passagem
    elif cidade == 'RECIFE':
        custo_da_passagem = 831.00
        return custo_da_passagem
    elif cidade == 'MANAUS':
        custo_da_passagem = 986.00
        return custo_da_passagem
    else:
        return 'Destino Invalido, Tente novamente!'












#Aluguel de Carro
#3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
#- Calcule o custo do aluguel do carro sendo que:
#- A cada dia o carro custa R$ 40,00;
#- Alugando 7 dias ou +: R$ 50,00 de desconto;
#- Alugando 3 dias ou +: R$ 20,00 de desconto;
#- Você pode receber apenas um desconto;
#- Retorne o custo."""


def custo_carro(dias):
    valor_carro = 40.0
    if dias >3 and dias <7:
        custo_carro = valor_carro * dias - 20.0
        return custo_carro
    elif dias >=7:
        custo_carro = valor_carro * dias - 40
        return custo_carro
    else:
        custo_carro = valor_carro * dias
        return custo_carro
'''

'       ''
Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!'''


def calculo_total(cidade, dias):
    total_hotel = custo_hotel(dias)
    total_aviao = custo_aviao(cidade)
    total_carro = custo_carro(dias)
    total = total_hotel + total_aviao + total_carro
    return total




#Gastos Extras
#5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
#Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais. 



def custoExtras(cidade, dias,gastos_extras):
    total_hotel = custo_hotel(dias)
    total_aviao = custo_aviao(cidade)
    total_carro = custo_carro(dias)
    extras = gastos_extras
    total_extras = total_hotel + total_aviao + total_carro + extras
    return total_extras


cidade = input('Escolha a cidade que deseja viajar:').strip().upper().replace('ã', 'a')
dias = int(input('Quantos dias durara sua viagem?'))
gastos_extras = float(input('Digite seus gastos extras R$:'))


print(f'''
Cidade:{cidade}
Dias:{dias}
Extras R$:{gastos_extras} reais
Valor total R$:{custoExtras(cidade, dias, gastos_extras):.2f} reais
''')