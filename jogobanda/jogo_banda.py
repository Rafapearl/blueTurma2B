1# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas et cetera

from time import sleep
from random import randint
import pygame


class Personagem:
    def __init__(self):
        self.habilidade = 0
        self.cansaco = 0
        self.fama = 0
        self.dinheiro = 0

    def multiplicativo(self):
        self.habilidade *= 1
        self.cansaco *= 1
        self.fama *= 1
        self.dinheiro *= 1

class Rockeiro(Personagem):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f'Você escolheu ser Rockeiro!!! Sua habilidade e seu público se desenvolverão mais rápido,\nporém não terás tanta fama nem dinheiro, pois nasceu na época errada!!!\nHabilidade: {self.habilidade}\nCansaço: {self.cansaco}\nFama: {self.fama}\nDinheiro: R$ ' + format(self.dinheiro,'.2f').replace('.',',') + '\n'
    
    def multiplicativo(self):
        
        self.habilidade *= 1.2
        self.cansaco *= 1.2
        
        

class Sertanejo(Personagem):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'Você escolheu ser Sertanejo!!! Sua fama e seu dinheiro se desenvolverão mais rápido,\nporém não terás tanta habilidade nem público, afinal o que importa mesmo é a conta no banco!!!\nHabilidade: {self.habilidade}\nCansaço: {self.cansaco}\nFama: {self.fama}\nDinheiro: R$ ' + format(self.dinheiro,'.2f').replace('.',',') + '\n'
    
    def multiplicativo(self):
        
        self.fama *= 1.2
        self.dinheiro *= 1.2
        

class Publico:

    def __init__(self):
        self.publico = 500
    
    def __str__(self):
        return f'Seu Público é {self.publico:.0f}!!!\n'

    def multiplicativo_publico(self):
        self.publico *= 1.2


def Musica1(): 

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_metallica.mp3')
    pygame.mixer_music.play()
    
def Musica2():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_iron.mp3')
    pygame.mixer_music.play()
    
def Musica3():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_restart.mp3')
    pygame.mixer_music.play()

def Musica4(): 

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_evidencias.mp3')
    pygame.mixer_music.play()

def Musica5():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_marrone.mp3')
    pygame.mixer_music.play()

def Musica6():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_telo.mp3')
    pygame.mixer_music.play() 

def sound_rain():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_rain.mp3')
    pygame.mixer_music.play()
    
def sound_entrada():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\corte_entrada.mp3')
    pygame.mixer_music.play()

def sound_intro():

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Projeto Jogo\Banda_T2B\projetoMusica.mp3')
    pygame.mixer_music.play()
    
def chuva():                                # função que dispara a chuva se o número aleatório gerado para a variável 'x' for igual a 1
    print('CHUVA!!!')
    print()
    print('O Show foi cancelado!!!')
    sound_rain()
    subiu_no_palco == False
    cumprimentou_publico == False
    personagem.cansaco = 0
    publico.publico *= 0.85 
    sleep(2)

def lista_musica():

    if estilo == '1':

        print ('Qual música você deseja tocar?: \n')
        print ('Pressione (1) para: Metallica - Master of Puppets')
        print ('Pressione (2) para: Iron Maiden - Fear of the Dark')
        print ('Pressione (3) para: Restart - Levo Comigo\n')
        musica = input('Opção: ')
        print()

        while musica != '1' and musica != '2' and musica != '3':
            print('Opção inválida!!!\n')
            musica = input('Opção: ') 
            
        if musica == '1':

            if personagem.habilidade < 50:

                print('Você ainda não tem habilidade para tocar essa música! Escolha outra!!!\n')           
                lista_musica()
            else:

                Musica1()
                personagem.fama += 30
                publico.publico += 200
                personagem.cansaco += 15
                personagem.habilidade += 40
                personagem.dinheiro += 200
                personagem.multiplicativo()
                publico.multiplicativo_publico()
                

                print("Parace que a sua fama aumentou após esse som!!!")
                print(f'A sua fama agora é: {personagem.fama:.0f}.\nPúblico atual: {publico.publico:.0f}\nCansaço: {personagem.cansaco:.0f}\nHabilidade: {personagem.habilidade:.0f}')
                print('Dinheiro:', format(personagem.dinheiro,'.2f').replace('.',','))

        if musica == '2':

            Musica2()
            personagem.fama += 25
            publico.publico += 150
            personagem.cansaco += 10
            personagem.habilidade += 30
            personagem.dinheiro += 100
            personagem.multiplicativo()
            publico.multiplicativo_publico()
            
            print('Ao som do Maiden, o público foi a loucura!')
            sleep (2)
            print(f'A sua fama agora é: {personagem.fama:.0f}.\nPúblico atual: {publico.publico:.0f}\nCansaço: {personagem.cansaco:.0f}\nHabilidade: {personagem.habilidade:.0f}')
            print('Dinheiro:', format(personagem.dinheiro,'.2f').replace('.',',')) 

        if musica == '3':

            Musica3()
            personagem.fama -= 20
            publico.publico -= 300
            personagem.cansaco += 5
            personagem.habilidade -= 10
            personagem.dinheiro += 50
            

            print('O seu público não esperava tanta ousadia...contenha-se!/n')
            sleep(2)
            print(f'Sua habilidade foi reduzida em 10 pontos. Restart faz você desaprender a tocar! Agora sua habilidade é de {personagem.habilidade:.0f}. ')
            print(f'A sua fama reduziu para: {personagem.fama:.0f}. Público ainda fiel: {publico.publico:.0f} e cansaço: {personagem.cansaco:.0f} ')   

    else:

        print ('Qual música você deseja tocar?: \n')
        print ('Pressione (1) para: Chitãozinho & Xororó - Evidências')
        print ('Pressione (2) para: Bruno & Marrone - Bijuteria')
        print ('Pressione (3) para: Michel Teló - Ah se eu te pego!\n')
        musica = input('Opção: ')
        print()

        while musica != '1' and musica != '2' and musica != '3':
            print('Opção inválida!!!\n')
            musica = input('Opção: ') 
            
        if musica == '1':

            if personagem.habilidade < 50:

                print('Você ainda não tem habilidade para tocar essa música! Escolha outra!!!\n')
                sleep (2)           
                lista_musica()
                
            else:

                Musica4()
                personagem.fama += 30
                publico.publico += 200
                personagem.cansaco += 15
                personagem.habilidade += 40
                personagem.dinheiro += 200
                personagem.multiplicativo()
                
                print("Parace que a sua fama aumentou após essa moda!!!")
                sleep (2)
                print(f'A sua fama agora é: {personagem.fama:.0f}.\nPúblico atual: {publico.publico:.0f}\nCansaço: {personagem.cansaco:.0f}\nHabilidade: {personagem.habilidade:.0f}')
                print('Dinheiro:', format(personagem.dinheiro,'.2f').replace('.',','))

        if musica == '2':

            Musica5()
            personagem.fama += 25
            publico.publico += 150
            personagem.cansaco += 10
            personagem.habilidade += 30
            personagem.dinheiro += 100
            personagem.multiplicativo()
            
            print('O público até ouviu a voz do Marrone! Parabéns!!!')
            sleep (2)
            print(f'A sua fama agora é: {personagem.fama:.0f}.\nPúblico atual: {publico.publico:.0f}\nCansaço: {personagem.cansaco:.0f}\nHabilidade: {personagem.habilidade:.0f}')
            print('Dinheiro:', format(personagem.dinheiro,'.2f').replace('.',','))

        if musica == '3':

            Musica6()
            personagem.fama -= 20
            publico.publico -= 300
            personagem.cansaco += 5
            personagem.habilidade -= 10
            personagem.dinheiro += 50
            

            print('O seu público não esperava tanta ousadia...contenha-se!/n')
            print(f'Sua habilidade foi reduzida em 10 pontos. Michel Teló faz você desaprender a tocar! Agora sua habilidade é de {personagem.habilidade:.0f}. ')
            print(f'A sua fama reduziu para: {personagem.fama:.0f}. Público ainda fiel: {publico.publico:.0f} e cansaço: {personagem.cansaco:.0f} ')   

if(__name__ == "__main__"):
    
    publico = Publico()   
    subiu_no_palco = False
    cumprimentou_publico = False
    cont = 0                                        # contador para para disparar a posssibilade de chuva a partir da segunda rodada.
    x = 0                                           # variável que receberá um número aletório em cada estapa, podendo causar a chuva quando 'x' receber o número 1.
    carreira = 0                                    # contador para imprir relatórios da carreira do personagem do jogo
    
    while True:                                     # contagem regressiva no início do jogo
            print("---")
            print('Bem vindo à banda Turma 2B!!!')
            print('O seu show começa em')
            for cont in range (5, -1, -1):
                print (cont)
                sleep(1)
            if cont == 0:
                break
    
    sound_intro()
    
    sleep(0.5)
    print('----------')
    print('Escolha seu estilo musical:')
    print('----------')
    print()
    print('1 - Rock')
    print('2 - Sertanejo')
    print()
    estilo = input('Opção: ')

    while estilo != '1' and estilo != '2':

        print('Opção Inválida!')
        estilo = input('Opção: ')
    
    if estilo == '1':
        personagem = Rockeiro()
        print(Rockeiro())
        sleep(2)
    else:
        personagem = Sertanejo()
        print(Sertanejo())
        sleep(2)
        
    while True:
      
        print(publico)
        sleep(1)   
        print('----------')
        print("Ações:")
        print('----------')
        print()
        print('1 - Subir no palco')
        print('2 - Cumprimentar o público')
        print('3 - Tocar uma música')
        print('4 - Fazer uma pausa')
        print('5 - Abandonar Palco')
        print('0 - Sair do jogo')
        print()
        opcao = input("Escolha sua ação: ")
        print()
        
        while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '0' :
            print('Opção inválida!!!\n')
            opcao = input("Escolha sua ação: ")

        if carreira <= 30:         

            if opcao == '1':
                if cont >= 2: 
                    x = randint(1,5)
                    if x == 1:
                        chuva()
                    else:
                        if subiu_no_palco == False:
                            personagem.fama += 5
                            publico.publico += 100
                            subiu_no_palco = True
                            sound_entrada()
                            print('Você subiu no palco e o mosh já começou a se formar, hoje tem roda punk!!!!\n')
                            sleep(1)
                        else:
                            print('Você já está no palco!\n')
                            sleep (2)
                            print()
                else:
                    if subiu_no_palco == False:
                            personagem.fama += 5
                            publico.publico += 100
                            subiu_no_palco = True
                            sound_entrada()
                            if estilo == '1':
                                
                                print('Você subiu no palco e o mosh já começou a se formar, hoje tem roda punk!!!!\n')
                                sleep (2)
                            else:
                                
                                print('Os berrantes anunciaram a sua entrada!!! Agora você está no palco!!!\n')
                                sleep (2)
                    else:
                        
                        print('Você já está no palco!\n')
                        sleep (2)

            if opcao == '2':
                if cont >= 2:
                    x = randint(1,5) 
                    if x == 1:
                        chuva()
                    else:
                        if subiu_no_palco == False:
                            if estilo == '1':
                                print('Vai cumprimentar quem? O Roadie??!! Suba no palco já!!!\n')
                                sleep (2)
                            else:
                                sleep (2)
                                print('Suba no palco cowboy! Sua plateia o aguarda!\n')
                        else:
                            if cumprimentou_publico == True:
                                print('Chega de cumprimentar!!! Comece a tocar!!!\n')
                                sleep (2)
                            else:
                                personagem.fama += 10
                                publico.publico += 100
                                cumprimentou_publico = True
                                print('Que artista!!! o público delira com a sua simpatia! Quase uma miss!!!\n')
                                
                                sleep(1)
                else:
                    if subiu_no_palco == False:
                        if estilo == '1':
                            print('Vai cumprimentar quem? O Roadie??!! Suba no palco já!!!\n')
                            sleep (2)
                        else:
                            print('Suba no palco cowboy! Sua plateia o aguarda!\n')
                            sleep (2)
                    else:
                        if cumprimentou_publico == True:
                            print('Chega de cumprimentar!!! Comece a tocar!!!\n')
                            sleep (2)
                        else:
                            personagem.fama += 10
                            publico.publico += 100
                            cumprimentou_publico = True
                            print('Que artista!!! o público delira com a sua simpatia! Quase uma miss!!!\n')
                            sleep(1)
                        
            if opcao == '3':
                if cont >= 2: 
                    x = randint(1,5)
                    if x == 1:
                        chuva()
                    else:
                        if subiu_no_palco == False:
                            print('O público pede a sua presença no palco! Suba já!\n')
                            sleep (2)
                        else:
                            if cumprimentou_publico == False:
                                if estilo == '1':
                                    print('Seja educado!!! Cumprimente sua plateia!!!\n')
                                    sleep (2)
                                else:
                                    print('Peão que se preze primeiro cumprimenta o público\n')
                                    sleep (2)
                            else:
                                if personagem.cansaco >= 60:
                                    print('Você está muito cansado!!! Melhor fazer uma pausa!!!\n')
                                    sleep (2)
                                else:
                                    lista_musica() 
                else:
                    if subiu_no_palco == False:
                        print('O público pede a sua presença no palco! Suba já!\n')
                        sleep (2)
                    else:
                        if cumprimentou_publico == False:
                            if estilo == '1':
                                print('Seja educado!!! Cumprimente sua plateia!!!\n')
                                sleep (2)
                            else:
                                print('Peão que se preze primeiro cumprimenta o público\n')
                                sleep (2)
                        else:
                            if personagem.cansaco >= 60:
                                print('Você está muito cansado!!! Melhor fazer uma pausa!!!\n')
                                sleep (2)
                            else:
                                lista_musica()         
                cont += 1
                
            if opcao == '4':
                if personagem.cansaco <= 40:
                    print('Tá cansado do quê??? Comece a tocar!!!')
                    sleep (2)
                else:
                    print('Nada melhor que um Toddynho e uma noite bem dormida!!!\nAgora você está renovado!!!')
                    sleep (2)
                    personagem.cansaco -= 40
                    publico.publico *= 0.85

            if opcao == '5':
                print('Você Abandonou o palco!')
                sleep (2)

                if personagem.dinheiro >= 1000:
                    personagem.dinheiro -= 1000
                    print('Você será multado em R$ 1000,00!!!')
                    sleep (2)
                else:
                    print('Você será multado em R$', format(personagem.dinheiro,'.2f').replace('.',','), '!!!')
                    personagem.dinheiro = 0
                personagem.fama *= 0.5
                publico.publico *= 0.25
                print (f'A sua fama agora é: {personagem.fama:.0f}. Público atual: {publico.publico:.0f} e cansaço: {personagem.cansaco:.0f} ')
                sleep(1)
                print ("Abandonei o palco porque quero e posso!") 
                sleep(1)

            if opcao == "0":
                break      

            carreira += 1
            
            if estilo == '1':
                if carreira == 5:                       
                    print('\nCOMEÇO DE CARREIRA!!!\n')
                    
                    if publico.publico < 500*1.2:
                        print("Você começou a sua carreira com a perna esquerda, melhore!")
                        sleep (2)
                        print('Ganhos do inicio da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    else:
                        print("O inicio da sua carreira é promissor, continue assim!!!")
                        print('Ganhos do inicio da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                                                              
                if carreira == 10:                      
                    print('\nMEIO DA CARREIRA\n')
                    if publico.publico < 1000*1.2:
                        print("A sua carreira  está no meio e você já parece um fracassado! Melhore a sua pontuação, looser!")
                        sleep (2)
                        print('Ganhos até meados da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    else:
                        print("Está indo muito bem, se continuar assim vai se aposentar como um Deus do Rock!!")
                        sleep (2)
                        print('Ganhos até meados da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                if carreira == 15:
                    print('\nDECLÍNIO DA CARREIRA\n')
                    if publico.publico <1500*1.2:
                        print ("Lamentável! A sua carreira está chegando ao fim e você está só o caco!")
                        sleep (2)
                        print('Ganhos até o final da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    else:
                        print ("Apesar da crise de meia idade e do leve declinio, você continua ganhando público!!!")
                        sleep (2)
                        print('Ganhos até o final da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
            
                if carreira == 20:  

                    print('\nAPOSENTADORIA\n')

                    if publico.publico <2000*1.2:
                        print('Sua Carreira foi por água a baixo! Uma vida disperdiçada!!')
                        sleep (2)
                    elif publico.publico >=2000*1.2 and publico.publico <=2300*1.2:    
                        print('Você teve uma boa carreira! Não foi um Hendrix, mas deu para o gasto!!!')
                        sleep (2)
                    else:
                        print('Você marcou a vida das pessoas! Que homem, que artista!!!!')
                        sleep(5)
                    print('Você se aposentou com R$', format(personagem.dinheiro,'.2f').replace('.',','), f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    exit()
            else:
                if carreira == 5:                       
                    print('\nCOMEÇO DE CARREIRA!!!\n')
                    
                    if publico.publico < 500:
                        print("Você começou a sua carreira com a perna esquerda, melhore!")
                        sleep (2)
                        print('Ganhos do inicio da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    else:
                        print("O inicio da sua carreira é promissor, continue assim!!!")
                        sleep (2)
                        print('Ganhos do inicio da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                                                              
                if carreira == 10:                      
                    print('\nMEIO DA CARREIRA\n')
                    if publico.publico < 1000:
                        print("A sua carreira  está no meio e você já parece um fracassado! Melhore a sua pontuação peão!")
                        sleep (2)
                        print('Ganhos até meados da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    else:
                        print("Está indo muito bem, se continuar assim vai se aposentar como um Rei do Rodeio!!")
                        sleep (2)
                        print('Ganhos até meados da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                if carreira == 15:
                    print('\nDECLÍNIO DA CARREIRA\n')
                    if publico.publico <1500:
                        print ("Lamentável! A sua carreira está chegando ao fim e você está só o caco!")
                        sleep (2)
                        print('Ganhos até o final da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    else:
                        print ("Apesar da crise de meia idade e do leve declínio, você continua ganhando público!!!")
                        sleep (2)
                        print('Ganhos até o final da Carreira: R$', format(personagem.dinheiro,'.2f').replace('.',','),f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
            
                if carreira == 20:           
                    print('\nAPOSENTADORIA\n')

                    if publico.publico <2000:
                        print('Sua Carreira foi por água a baixo! Uma vida disperdiçada!!')
                        sleep (2)
                    elif publico.publico >=2000 and publico.publico <=2300:   
                        print('Você teve uma boa carreira! Não foi um Tião Carreiro, mas deu para o gasto!!!')
                        sleep (2)
                    else:
                        print('Você marcou a vida das pessoas! Que homem, que artista!!!!')
                        sleep(2)
                    print('Você se aposentou com R$', format(personagem.dinheiro,'.2f').replace('.',','), f'/ Fama: {personagem.fama:.0f}/ Público: {publico.publico:.0f}.')
                    
                    exit()