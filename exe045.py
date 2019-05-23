import random
jogador = int(input('[0] PEDRA, [1] PAPEL, [2] TESOURA'))
computador = random.randint(0,2)
if(computador == 0 and jogador == 2):
    print('Computador{} ganhou de'.format(jogador[computador]))