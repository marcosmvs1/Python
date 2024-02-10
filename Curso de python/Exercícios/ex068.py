# Exercicio par ou impar 

import random

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

while True:
    valor = int(input('Diga um valor: ')) 
    #opção = str(input('Par ou ímpar? [P/I]')) .upper() .lower() [0]
    comp = random.randint(1,10)
    print(comp)
    valor = valor + comp
    print(valor)
    resto = valor % 2

    if resto == 0:
        break
    else:
        print('-'*30)
print(f'PROGRAMA TABUADA ENCERRAD0. Volte sempre! ')