valor = int(input('Valor da casa? '))
salario = int(input('Seu salario?' ))
ano = int(input('Em quantos anos irá pagar? '))
ano=ano * 12
mensalidade = valor // ano
print('A mensalidade será de {}R$'.format(mensalidade))
if(mensalidade < salario*0.3):
    print('Emprestimo aprovado: ')
else:
    print('Emprestimo reprovado')