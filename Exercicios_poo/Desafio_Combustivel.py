'''Classe Bomba de Combustível
a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro.
iii. quantidadeCombustivel.
b. A classe deve possuir no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
foi colocada no veículo.
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
a ser pago pelo cliente.
iii. alterarValor( ) – altera o valor do litro do combustível.
iv. alterarCombustivel( ) – altera o tipo do combustível.
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.'''


class bombaCombustível:
    def __init__(self, tipocombustivel, valorLitro, quantidadeCombustivel):
        self.tipocombustivel = tipocombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def __str__(self):
        return f"{self.tipocombustivel}:{self.valorLitro :02d}: {self.quantidadeCombustivel}"

    def abastecerPorValor(self):
        ValorInput = float(input("Digite qual é o valor que deseja abastecer: "))
        custo = ValorInput  
        print (custo)
        #print (tipo)
        #tipo2 = tipo 
        #quantidade = float(input("Digite quasto litros deseja abastecer: "))
        #quantidadeporL = quantidade * valor
        #self.quantidadeCombustivel = self.quantidadeCombustivel - quantidade
        #print (f"O valor da {tipo2} é R$ {valor} por litro, você abasteceu {quantidade} litros por R$ {quantidadeporL:.2f}")



        print (f'Agora  o posto possui o total de: {self.quantidadeCombustivel} litros de gasolina')

    def abastecerPorLitro (self):
        print (tipo)
        tipo2 = tipo 
        quantidade= float(input("Digite quasto litros deseja abastecer: "))
        quantidadeporL = quantidade * valor
        self.quantidadeCombustivel = quantidadetotal - quantidade
        print (f"O valor da {tipo2} é R$ {valor} por litro, você abasteceu {quantidade} litros por R$ {quantidadeporL:.2f}")
        
        print (f'Agora  o posto possui o total de: {self.quantidadeCombustivel} litros de gasolina')

valor = 0
tipo = input ("Digite qual é o tipo do combustivel: ").lower()
tipo2 = tipo
quantidadetotal = 1000
quantidade = 0

if tipo == "gasolina":
    valor = 4.5
elif tipo == "diesel":
    valor = 4.2
elif tipo == "etanol":
    valor = 3.7

        
a = bombaCombustível(tipo, valor, quantidade)
a.abastecerPorValor()
#a.abastecerPorLitro()
