# Exercicio par ou impar 

from random import randint

v = 0
while True:
    print('-=' *20)
    print('VAMOR JOGAR PAR OU ÍMPAR ')
    print('-=' *20)
    jogador = int(input('Digite um número: '))
    comp = randint(1,10)
    total = comp + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar ')).lower() .upper() [0]
    print(f'Você jogou {jogador} e o computador {comp}. Total de {total}')
    print('DEU PAR' if total % 2 == 0  else 'DEU IMPAR') 
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!! ')
            v = v + 1
        else:
            print('Você perdeu!!!!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu!!! ')
            v = v + 1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamnte...')
print(f'GAME OVER!!! Você venceu  {v} vezes')
        

   

