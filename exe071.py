cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
dinheiro = int(input("Digite o valor a ser sacado"))

while(dinheiro >0):
    if (dinheiro % 100 == 0):
         cem +=1
         dinheiro -= 100
    elif (dinheiro % 50 == 0):
        cinquenta +=1
        dinheiro-=50
    elif(dinheiro % 20 == 0):
        vinte+=1
        dinheiro-=20
    elif(dinheiro % 10 == 0):
        dez+=1
        dinheiro-=10
    elif(dinheiro % 5 == 0):
        cinco+=1
        dinheiro-=5
    elif(dinheiro % 2 == 0):
        dois+=1
        dinheiro-=2
    elif(dinheiro % 1 == 0):
        um+=1
        dinheiro-=1
print("Foram usadas {} notas de 100".format(cem))
print("Foram usadas {} notas de 50".format(cinquenta))
print("Foram usadas {} notas de 20".format(vinte))
print("Foram usadas {} notas de 10".format(dez))
print("Foram usadas {} notas de 5".format(cinco))
print("Foram usadas {} notas de 2".format(dois))
print("Foram usadas {} notas de 1".format(um))