vel = float(input('Qual velocidade do carro: '))

if vel > 80:
    print(f'Você foi multado! O valor da multa é de R${(vel - 80) * 7}')
else:
    print('Você não foi multado: ') 