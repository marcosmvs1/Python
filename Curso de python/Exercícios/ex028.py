import random
sorteio = random.randrange(6)
print(sorteio)
num = int(input('Tente adivinhar o número do sorteio: '))
if sorteio == num:
    print(f'O número sorteado foi {sorteio} PARABÉNS VOCÊ ACERTOU!!')
else:
    print(f'O número sorteado foi {sorteio} Você errou, tente novamente')
    