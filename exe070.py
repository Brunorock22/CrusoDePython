print("--" * 30)
print("LOJA")
print("--" * 30)
cont = "s"
preco = 0
menor = 100000000
total = 0
caro = 0
nome = str
produto = str
while cont == "s":
    nome = str(input("Nome do produto: "))
    preco = int(input("Preço: "))
    total += preco
    if preco > 1000:
        caro += 1
    if preco < menor:
        menor = preco
        produto = nome
    cont = str(input("Deseja continuar :[S/N]")).lower()
print("----------- FIM DO PROGRAMA --------------")
print('Total da compra foi {}R$'.format(total))
print('Temos {} produto acima de 1,000R$'.format(caro))
print('O produto mais barato foi {} custando {}R$'.format(produto, menor))
