dis = float(input('Qual distância da sua viagem: '))
dis1 = dis * 0.50
dis2 = dis * 0.45
print(dis1)

if dis > 200:
    print(f'Sua viagem vai custar R${dis2}')
else:
    print(f'Sua Viagem vai custar R${dis1}')