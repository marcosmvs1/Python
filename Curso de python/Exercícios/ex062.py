print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primero termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont1 = 1
cont2 = 1 
while cont1 <= 10:
    print(f' {termo} > ')
    cont1 += 1
    termo = termo + razão

cont2 = int(input('Quantos termos você quer mostrar a mais: '))    
if cont2 >= 1:
    cont1 = 1
    print('looping')
else:
    print('FIM')


'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primero termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f' {termo} > ', end= '')
    cont += 1
    termo = termo + razão
    '''





  


