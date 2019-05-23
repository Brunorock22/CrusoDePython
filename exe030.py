n = int(input('\033[33mDigite um numero '))
r = n % 2
if r == 0:
    print('O numero {} é \033[31mPar'.format(r))
else:
    print('O numero {} é Impar'.format(r))