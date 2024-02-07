import random

def jogo_de_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número entre 1 e 10.")
    print("Você tem uma chance de 40% de acertar.")

    numero_secreto = random.randint(1, 10)

    tentativas = 3
    chance_acerto = 40

    while tentativas > 0:
        print("\nTentativas restantes:", tentativas)
        palpite = int(input("Digite sua aposta (entre 1 e 10): "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            return
        elif random.randint(1, 100) <= chance_acerto:
            print("Você errou! O número era", numero_secreto)
            return
        else:
            print("Você errou! Tente novamente.")
            tentativas -= 1

    print("\nVocê usou todas as tentativas. O número secreto era", numero_secreto)

jogo_de_adivinhacao()
