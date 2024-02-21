#importando somente funções da biblioteca 
from math import floor,sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.1F} ')
print(f'A raiz de {num} é igual a {floor(raiz)}')
