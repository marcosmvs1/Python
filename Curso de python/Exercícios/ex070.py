# PROGRAMA PARA CADASTRO DE PESSOAS 
total = totmil = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço

    if preço > 1000:
        totmil += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor  = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]")) .strip() .upper() [0]
    if resp == 'N':
        break
print(f' ------ Fim do programa -------')
print(f'O total da compra foi R$ {total}')
print(f'Temos {totmil} produtos que custaram mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor}')