compra = float(input('Preço das compras:  R$ '))

print('''Escolha uma das bases para a conversão:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão ''')

opção = int (input('Sua opção: '))

opção1 = compra - ((compra * 10) / 100) 
opção2 = compra - ((compra * 5) / 100) 
opção4 = compra + ((compra * 20) / 100) 

if opção == 1:
    print(f''' Sua compra será à vista no dinheiro. DE R${compra} você vai pagar R${opção1:.2F}''')

elif opção == 2:
    print(f''' Sua compra será à vista no cartão. DE R${compra} você vai pagar R${opção2:.2F}''')

elif opção == 3:
    parcela = compra / 2
    print(f'''Sua compra será parcelada em 2x de {parcela:.2F} SEM JUROS 
Sua compra de {compra:.2F} vai custar {compra:.2F} ''')

elif opção == 4:
    qtd = int(input('Quantas parcelas: '))
    print(f'''Sua compra será parcelada em {qtd}x de {opção4 / qtd :.2F} COM JUROS DE 20%
Sua compra de {compra:.2F} vai custar {opção4:.2F} ''')





