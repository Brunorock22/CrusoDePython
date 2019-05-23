from datetime import datetime
now = datetime.now()
atual = now.year
menor=0
for c in range(1,3):
    pessoa = int(input('data de nascimento da {}º pessoa '.format(c)))
    verificar = atual-pessoa
    if verificar<18:
        menor = menor+1
if (menor == 0 ):
    print('Não há menores de idade na lista')
else:
    print('Nesta lista há {} pessoas menores de idade'.format(menor))