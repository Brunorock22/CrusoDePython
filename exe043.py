peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
resultado = peso/(altura**2)
print('Seu indice é resultado {}'.format(resultado))
if resultado < 18.5:
    print("Abaixo do peso")
elif resultado <24.9:
    print("Peso normal")
elif resultado <29.9:
    print('Sobrepeso')
elif resultado < 34.9:
    print('Obesidade')
else:
    print('JESSICA')