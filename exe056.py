media = 0
novinhas = 0
for c in range(1,5):
    print(20*"=--=")
    print("{}ª Pessoa".format(c))
    nome=str(input("Nome: "))
    idade=int(input('Idade: '))
    sexo=str(input("[M/F]")).lower()
    media =(media+idade)
    if sexo == 'm':
        if c == 1:
            velho = nome
            maior = idade
        else:
            if idade > maior:
                velho = nome
                maior = idade
    if sexo == 'f':
        if(idade <20):
            novinhas = novinhas+1
print(20*"=--=")
print('A média de idade do gropo é de {}'.format(media/4))
print('O homem mais velho é o {} com {} anos'.format(velho,maior))
print('Ao todo são {} mulheres cm menos de 20 anos'.format(novinhas))