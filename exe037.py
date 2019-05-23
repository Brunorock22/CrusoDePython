numero = int(input('Digite um numero: '))

opcao =0
while(opcao !=4 ):
    print('=' * 10)
    print('MENU [1]BINARIO,[2]OCTAL, [3]HEXADECIMAL, [4]SAIR')
    opcao = int(input('Sua opão :'))
    if opcao == 1:
        print('O resultado em binario sera {}'.format(bin(numero)[2:]))
    elif opcao ==2 :
        print('O resultado em binario sera {}'.format(oct(numero)[2:]))
    elif opcao ==3:
        print('O resultado em binario sera {}'.format(hex(numero)[2:]))
    else:
        print('Digite uma opcão valida')

