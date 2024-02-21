from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções: 
      [ 0 ] PEDRA
      [ 1 ] PAPEL 
      [ 2 ] TESOURA''')
player = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 10)
print(f'Computador jogou {comp}')
print(f'Jogador jogou {player}')
print('-=' * 10)
if comp == 0:
    sleep(2)
    if player == 0:
        print('Empate ')
    
    elif player == 1:
        print('Jogador win')

    elif player == 2:
         print('Computador win ')
        
    else:
        print('jogada inválida ')

elif comp == 1:
    sleep(2)
    if player == 0:
        print('jogador Win!!!')
    
    elif player == 1:
        print('Empate ')

    elif player == 2:
         print('Computador Win!!! ')
        
    else:
        print('jogada inválida ')

elif comp == 2: 
    sleep(2)
    if player == 0:
        print('jogador Win!!!')
    
    elif player == 1:
        print('Computador Win!!! ')

    elif player == 2:
         print('Empate ')
        
    else:
        print('jogada inválida ')
