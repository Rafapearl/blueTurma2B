from time import sleep

class Personagem:
    def __init__(self):
        self.habilidade = 50
        self.cansaco = 0
        self.fama = 0
        self.dinheiro = 0
        self.cache = 1000
    
    def __str__(self):
       return f'Sua habilidade é, {self.habilidade}, Seu cansaço é, {self.cansaco}, Sua fama é {self.fama}, e sua conta bancária é {self.dinheiro}.'

class Publico:
    def __init__(self):
        self.publico = 500
 
if(__name__ == "__main__"):
    
    personagem = Personagem()
    publico = Publico()   
    
    while True:
        print("---")
        print('Bem vindo à banda Turma 2B!!!')
        print('O seu show começa em')
        for cont in range (5, -1, -1):
            print (cont)
            sleep(1)
        if cont ==0:
            break
    while True:
        print(personagem)
        print("")
        print("Ações:")
        print('1 - Cumprimentar o público')
        print('2 - Tocar uma música')
        print('3 - Abandonar Palco')
        print('0 - Sair')
        opcao = input('Escolha sua ação: ')
        if opcao == '1':
            print('Quanto carisma! Eis um grande artista!!!')
            personagem.fama += 5
            publico.publico += 100
            
        
        if opcao =='2': 
            print ('Qual música você deseja tocar?: ')
            print ('Pressione (1) para:  Metallica - Master of Puppets')
            print ('Pressione (2) para: Iron Maiden - Fear of the Dark')
            print ('Pressione (3) para: A se eu te pego!')
            musica = input ('opção: ') 
        if musica == '1':    
            personagem.fama += 30
            publico.publico += 200
            personagem.cansaco += 15
            print ("Parace que a sua fama aumentou após esse som!!!")
            print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            
        if musica == '2':
            personagem.fama += 25
            publico.publico += 150
            personagem.cansaco += 10
            print ('Ao som do Maiden, o público foi a loucura!')
            print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
        

        if musica == '3':
            personagem.fama -= 20
            publico.publico -= 300
            personagem.cansaco += 5
            print ('O seu público não esperava tanta ousadia...contenha-se!')
            print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            

    

            
        
        if opcao == '3':

            personagem.fama -= 10
            print (f'A sua fama agora é: {personagem.fama}. Público atual: {publico.publico} e cansaço: {personagem.cansaco} ')
            print ("Abandonei o palco porque quero e posso!")

            

       # print(f'Sua habilidade é, {personagem.habilidade}, Seu cansaço é, {personagem.cansaco}, Sua fama é {personagem.fama}, e sua conta bancária é {personagem.dinheiro}.')
