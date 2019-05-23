n = 0
cont = total = 0
while(n != 999):
    n = int(input("Digite 999 para parar e calcular "))
    total = total + n
    cont += 1
print("A soma dos {} valores é : {}".format(cont,total))