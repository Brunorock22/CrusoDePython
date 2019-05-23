numero = int(input("\033[33mDigite um numero para ver sua tabuada: "))
for c in range (1,11):
    print("{} X {} = {}".format(numero,c,(numero*c)))