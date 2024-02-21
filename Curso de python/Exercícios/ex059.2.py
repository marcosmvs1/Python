from time import sleep
valor1 = int (input('Primeiro valor: '))
valor2 = int (input('Segundo valor: '))

opção = 0
while opção != 5:
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do pragrama')
    print('='*20)
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = valor1 + valor2
        print('Calculando...')
        sleep(1)
        print('Processando... Só um minuto....')
        sleep(2)
        print('='*40)
        print(f'===== ( A soma entre {valor1} + {valor2} é {soma} )===== ')
        
    
    elif opção == 2:
        multiplica = valor1 * valor2
        print(f'A multiplicação entre {valor1} X {valor2} é {multiplica} ')
        

    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else: 
            maior = valor2
        print(f'Entre {valor1} e {valor2} o maior valor é  {maior} ')
        
    
    elif opção == 4:
        valor1 = int (input('Primeiro valor: '))
        valor2 = int (input('Segundo valor: '))
        
    
    elif opção == 5:
        print('Finalizando...')


    else:
        print('Opção invalida. Tente novamente')
    
    print('='*40)
    sleep(2)
    
 

print('FIm')