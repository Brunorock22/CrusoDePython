print("Sequencia de Fibonacci :")
n = int(input("Quantos termos deseja mostrar? "))
atual = 0
proximo = 1
c = 3
print("{} {}".format(atual,proximo), end='')
while (c <= n):
    res = atual+proximo
    print(" {} ".format(res), end='')
    atual = proximo
    proximo = res
    c+=1