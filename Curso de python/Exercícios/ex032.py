ano = int(input('digite um ano: '))
rest = ano % 4 == 0
if rest == True:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} Não é um ano bissexto')  
