n1 = int(input('PA :'))
n2 = int(input('Razão :'))
termo = n1
c = 1
while c <= 10:
    print('{} '.format(n1), end='')
    n1 = n1 + n2
    c += 1