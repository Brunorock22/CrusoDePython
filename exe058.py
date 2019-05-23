from random import randint
print('Advinhe um numero entre 0 a 10')
numero = int(input('Qual seu palpite? '))
aleatorio = randint(0,10)
while(numero != aleatorio):
    if(numero > aleatorio):
        numero = int(input('Menos... tente novamente :'))
    else:
        numero = int(input('Mais... tente novamente :'))
print('Você acertou eu pensei no numero {}'.format(aleatorio))