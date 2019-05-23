a = int(input('Primeiro lado do triangulo: '))
b = int(input('Segundo lado do triangulo: '))
c = int(input('Terceiro lado do triangulo: '))

if(a<b+c and  b<a+c and c<a+b ):
    print('Este é um triangulo valido')
else:
    print('Triangulo invalido')