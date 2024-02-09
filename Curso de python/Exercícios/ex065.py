#Exercicio 65 Maior e menor valor
resp = 'S'
soma = quant = media = maior = menor =0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else: num 
    

    resp = str(input('Quer continuar? [S/N]? ')).upper() .strip() [0]

print(f'Você digitou {quant} números e média foi {media}' ) 
print(f'O maior valor foi {media}')