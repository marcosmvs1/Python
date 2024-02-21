from datetime import date

ano = int(input('digite um ano: '))

if ano == 0: 
    ano = date.today().year
 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'"O\033[4;30;45m {ano}\033m" é um ano bissexto')
else:
    print(f'{ano} Não é um ano bissexto')  
