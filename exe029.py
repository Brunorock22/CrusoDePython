velocidade = int(input('Digite a velocidade do seu carro! '))

if velocidade > 80:
    print('Multado,o limite é de 80 km/h')
    multa = (velocidade-80)*7
    print(' O valor da multa será: {}'.format(multa))
print('Digite com o segurança: ')