nome = str(input('Digite seu nome completo'))
separa = nome.split()
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu ultimo nome é {} '.format(separa[len(separa)-1]))
