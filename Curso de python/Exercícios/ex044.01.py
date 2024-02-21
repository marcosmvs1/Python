compra = float(input('Preço das compras:  R$ '))

print('''Escolha uma das bases para a conversão:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão ''')

opção = int (input('Sua opção: '))
 

opção4 = compra + ((compra * 20) / 100) 

if opção == 1:
    opção1 = compra - ((compra * 10) / 100) 
   
elif opção == 2:
    opção1 = compra - ((compra * 5) / 100) 

elif opção == 3:
    opção1 = compra
    parcela = opção1 / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2F} SEM JUROS')

elif opção == 4:
    opção1 = compra + ((compra * 20) / 100) 
    qtd = int(input('Quantas parcelas: '))
    print(f'Sua compra será parcelada em {qtd}x de {opção1 / qtd :.2F} COM JUROS DE 20% ')

print(f'Sua compra de R$: {compra:.2F} vai custar {opção1:.2F} no final ')




