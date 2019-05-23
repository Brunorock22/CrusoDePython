from datetime import datetime
ano = int(input('Digite o ano de seu nascimento: '))
now = datetime.now()
idade = now.year - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, now.year))


if idade < 18:
    print('Você se alistara em {}, por tanto faltam {} anos'.format(ano+18, ano+18-now.year))
elif idade > 18:
    print('Você tinha se alistar em {}'.format(ano+18))
else:
    print('Você tem 18 anos em {}'.format(now.year))