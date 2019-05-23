import random
from time import sleep
print('=--='*20)
n = int(input('Pense em um numero entre 0 a 5 ! '))
print('=--='*20)
computador = random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print('=--='*20)
if n == computador:
    print(' Voce Advinhou ,eu pensei no {}'.format(computador))
else:
    print('Você perdeu ! eu pensei no {}'.format(computador))