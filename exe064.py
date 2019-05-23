n = 0
c = 0
soma = 0
while(n != 999):
    c += 1
    n = int(input("Digite um numero : [999 parar parar]"))
    soma = n + soma
print('Você digitou {} numeros e a soma deles é {}'.format(c-1,soma-999))