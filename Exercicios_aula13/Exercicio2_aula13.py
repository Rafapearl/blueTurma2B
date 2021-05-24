# 2. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feito em cada partida. No final tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.


dicioj = dict()
gol = []
NomeJogador = input("Qual é o nome do jogador?: ")
Npartidas = int(input("Quantas partidas essse jogador jogou?: "))
TotalGol = 0


for item in range (1, Npartidas +1):
    golpartida = int(input(f"Quantos gols o jogador {NomeJogador} fez na partida {item}?: "))

    gol.append(golpartida)
    TotalGol = TotalGol + golpartida


print (TotalGol)

