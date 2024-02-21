#Simulador de caixa eletrônico 
ced1 = ced10 = ced20 = ced50 = 1
cont = 0
while True:
    print('='*40)
    print('             BANCO DO MARCÃO')
    print('='*40)
    valor = int(input('Qual valor você quer sacar: R$ '))
    for c in range(1, 5): 
        print(f'{valor} DIVIDO POR  {c} = {valor / c} ')
   
