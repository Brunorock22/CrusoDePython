from datetime import date
ano = int(input('Qual ano deseja analisar?Digite 0 para verificar o ano atual '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('Ano bisexto')
else:
    print('Ano não é bisexto')