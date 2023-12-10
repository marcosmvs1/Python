a = int(input('Primeiro valor: '))
b = int (input('Segundo valor: '))
c = int (input('Terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c 
print(f'o menor valor foi {menor}')

maior = a 
if b > a and b > c:
    maior = b 
if c > b and c > a: 
    maior = c
print(f'O maior número é {maior}')





# não fiz