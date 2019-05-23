menu = 0
while (menu != 5):
    print(20*'=--=')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    menu = int(input('\n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos numeros \n[5]sair \n'))
    if menu == 1:
        soma = n1+n2
        print(('{} + {} = {}').format(n1,n2,soma))
    if menu == 2:
        multiplicacao = n1*n2
        print('{} * {} = {}'.format(n1,n2,multiplicacao))
    if menu == 3:
        if n1 > n2:
            print('O maior é o {}'.format(n1))
        else:
            print('O maior é o {}'.format(n2))
    if menu == 4 :
        print('Digite novamente: ')

print('Você saiu do programa!')