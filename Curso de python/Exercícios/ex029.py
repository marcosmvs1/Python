vel = float(input('Qual velocidade do carro: '))
cal = (vel - 80) * 7

if cal > 1:
    print(f'Você foi multado! O valor da multa é de R${cal:1F}')
else:
    print('Você não foi multado: ') 