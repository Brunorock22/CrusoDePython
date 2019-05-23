a = int(input('Primeiro lado '))
b = int(input('Segundo lado '))
c = int(input('Terceiro lado '))
if a <b+c and b < a+c and c<a+b:
    if a==b or a==c or b==c:
        print('Triangulo Isoceles')
    elif a!= b and b != c and a != c:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Equilatero')
else:
    print('Não é um triangulo')