n=1
while n > 0:
    n = int(input("Digite um valor: "))
    for i in range (1,11):
        resultado = i * n
        print("{} x {} = {}".format(n,i,resultado))