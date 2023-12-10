med1 = float(input('Digite 3 medidas para saber se forma um triangulo\nMedida 1: '))
med2 = float(input('Medida 2: '))
med3 = float(input('Medida 3: '))
cond1 = med1 + med2 > med3
cond2 = med2 + med3 > med1
cond3 = med1 + med3 > med2 == True

print(cond1)

'''if cond1,
    print(f'As medidas {med1, med2, med3} formam um triângulo')
else:
    input('As medidas não formam um triangulo')'''