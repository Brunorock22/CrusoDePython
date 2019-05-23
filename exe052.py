primo=0
numero = int(input('Digite um numero: '))
print("="*30)
for c in range(1,numero+1):
    if(numero % c == 0):
        primo+= 1
if (primo == 2 or numero ==1):
    print("Este numero é primo!!!")
else:
    print("Este numero não é primo")

