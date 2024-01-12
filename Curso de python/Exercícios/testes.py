print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primero termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais = 10
while mais != 0:
    while cont <= mais:
        print(f' {termo}  ', end= '')
        
        cont += 1
        termo += razão
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais: ')) 
    

print('FIM!!!')   
    


