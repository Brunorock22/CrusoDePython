print("--" * 30)
print("CASTRE UMA PESSOA")
print("--" * 30)
cont = "s"
maior = 0
mulherIdade = 0
homem = 0
while cont == "s":
    idade = int(input("Idade: "))
    sexo = str(input("[M/F]")).lower()
    print("--"*30)
    if idade >= 18:
        maior += 1
    if sexo == "m":
        homem += 1
    if sexo == "f":
        if idade < 20:
            mulherIdade += 1
    cont = input("Deseja continuar ? [S/N]").lower()
print("Total de pessoas cm mais de 18 : {}".format(maior))
print("Total de homens : {}".format(homem))
print("Mulheres cm menos de 20 anos : {}".format(mulherIdade))