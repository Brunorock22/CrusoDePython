maior=0
menor =0
for c in range (1,6):
    peso = float(input("Didite seu peso: "))
    if c == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso sera {} e o menor é de {}'.format(maior,menor))