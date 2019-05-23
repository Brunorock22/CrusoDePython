preco = int(input('Valor da conta: '))
opcao = int(input('''
[1] Valor a Vista,
[2] Avista no cartao,
[3] 2 x no cartão, 
[4] 3 x no cartão: '''))
if(opcao == 1):
    desconto = preco-(preco * 0.1)
    print('Com desconto de 10 % pagara: {}R$'.format(desconto))
elif(opcao == 2):
    desconto = preco-(preco*0.05)
    print('Com desconto de 5% pagara :{}R$'.format(desconto))
elif(opcao==3):
    print('2 x no valor normal:{}R$'.format(preco))
elif(opcao==4):
    desconto = preco+(preco*0.20)
    print('3x com juros de 20% pagara {}R$'.format(desconto))