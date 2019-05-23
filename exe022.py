nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print(nome.__len__()-nome.count(' '))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa=nome.split()
print('Seu nome é {} e ele tem {} letras'.format((separa[0], len(separa[0]))))