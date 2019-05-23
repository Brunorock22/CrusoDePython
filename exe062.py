n1 = int(input('PA :'))
n2 = int(input('Razão :'))
termo = n1
c = 1
while c <= 10:
    print('{}='.format(n1), end='')
    n1 = n1 + n2
    c += 1
sequencia = 1
contador = 0
while(sequencia != 0):
    sequencia = int(input("\nQuantos termos deseja mostrar a mais? "))
    for c in range(1, sequencia+1):
        print('{}='.format(n1), end='')
        n1 = n1 + n2
        contador = c+contador
print("Progressão finalizada com {} termos".format(contador+10))
