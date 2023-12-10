import random
from time import sleep
sorteio = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-'*20)
num = int(input('Tente adivinhar o número do sorteio: '))
print('PROCESSANDO...')
sleep(3)
if sorteio == num:
    print(f'O número sorteado foi {sorteio} PARABÉNS VOCÊ ACERTOU!!')
else:
    print(f'O número sorteado foi {sorteio} Você errou, tente novamente')
    