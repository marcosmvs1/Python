import random
from time import sleep
computador  = random.randint(0,10)

print('-=-'*20)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
print('-=-'*20)

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpites += 1
    print('PROCESSANDO...')
    sleep(0.5)
    
    if jogador == computador:
        acertou = True

    else:
        if jogador < computador :
            print(f'Dica: É UM NÚMERO MAIOR ')
        if jogador > computador:
            print('Dica: É UM NÚMERO MENOR')
print(f'Acertou com {palpites} tentativas. PARABÉNS!!')

        