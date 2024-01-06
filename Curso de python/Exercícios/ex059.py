
r = '0'
while r not in '5': 
    valor1 = int (input('Primeiro valor: '))
    valor2 = int (input('Segundo valor: '))
    opção = int (input('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do pragrama \nQual sua opção:  '))
    if opção == 1:
        soma = valor1 + valor2
        print(f'{valor1} + {valor2} = {soma}')
        r = str(input('Quer continuar? Digite (S) para sim ou (N) para não: ')).upper()
        if r == 'S':
            r = '0'
        elif r == 'N':
            r = '5'
                
                
    if opção == 2:
        multiplica  = valor1 * valor2
        print(f'{valor1} X {valor2} = {multiplica}')
        r = str(input('Quer continuar? Digite (S) para sim ou (N) para não: ')).upper()
        if r == 'S':
            r = '0'
        elif r == 'N':
            r = '5'

    if opção == 3:

        maior = 0
        if valor1 > valor2:
            maior = 'Primeiro valor'
            print(f'O maior número digitado foi {maior} que é: {valor1}')
            r = str(input('Quer continuar? Digite (S) para sim ou (N) para não: ')).upper()
        if r == 'S':
            r = '0'
        elif r == 'N':
            r = '5'


        elif valor1 == valor2:
            print('O Primeiro e o segundo número são iguais ')
            r = str(input('Quer continuar? Digite (S) para sim ou (N) para não: ')).upper()
        if r == 'S':
            r = '0'
        elif r == 'N':
            r = '5'
        
        else:
            maior = 'Segundo valor'
            print(f'O maior número digitado foi o {maior} que é: {valor2}') 
            r = str(input('Quer continuar? Digite (S) para sim ou (N) para não: ')).upper()
        if r == 'S':
            r = '0'
        elif r == 'N':
            r = '5'
    if opção == 4:
        r = '0'

    if opção == 5:
        r = '5'
    
    
print('FIM!!!!')



