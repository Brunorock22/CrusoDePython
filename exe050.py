contador = 0
for c in range(1,7):
    numeros=int(input("Digete o {}º numero: ".format(c)))
    if numeros % 2 == 0:
        contador += numeros
print(contador)