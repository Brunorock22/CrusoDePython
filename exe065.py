res = str("s")
cont = 0
n = 0
max = 0
min = 0
total = 0
media = 0
while(res == "s"):
    n = int(input("Digite um numero: "))

    if (cont == 0):
        max = n
        min = n
    else:
        if (n >= max):
            max =  n
        if(n < min):
            min = n
    res =input("Deseja continuar ?")
    cont += 1
    total = n + total
print("Maior valor = {}".format(max))
print("Menor valor = {}".format(min))
print("Quantidade de numeros = {}".format(cont))
media = total / cont
print("A media é {}".format(round(media,2)))
