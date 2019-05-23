salario = int(input('Digite seu salario '))
if(salario < 1250):
    x=salario*0.15+salario
    print('Salario menor que a base ajustado para {}'.format(x))

if(salario>=1250):
    x=salario*0.1+salario
    print('Salario superior a base ajustado para {}'.format(x))