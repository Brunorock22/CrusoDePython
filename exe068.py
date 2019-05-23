import random
par = 0
impar = 0
for c in range(1, 3):
    dedos = int(input("Digite um valor: "))
    decisao = input("[P/I] ").lower()
    computador = random.randint(0, 10)
    total = dedos+computador
    print("--"*20)
    if total % 2 == 0:
        if decisao == "p":
            print("Você acertou :\n")
            print("0Jogou {} e o computador {}.Total de  {} deu PAR ".format(dedos, computador, total))
        elif decisao == "i":
            print("Você acertou :\n")
            print("1Jogou {} e o computador {}.Total de  {} deu IMPAR ".format(dedos, computador, total))
    elif total % 2 == 1:
        if decisao == "i":
            print("Você acertou :\n")
            print("2Jogou {} e o computador {}.Total de  {} deu IMPAR ".format(dedos, computador, total))
        else:
            print("Você errou :\n")
            print("3Jogou {} e o computador {}.Total de  {} deu PAR ".format(dedos, computador, total))
    print("---------------------------------")