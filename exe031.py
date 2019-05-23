distancia = int(input('Digite a distancia da viagem: '))
if distancia < 200:
    preco = distancia * 0.5
    print('O preço da distancia sera de {}R$'.format(preco))
else:
    preco = distancia * 0.45
    print('Viagem acima de 200 km o preço será de {}R$'.format(preco))