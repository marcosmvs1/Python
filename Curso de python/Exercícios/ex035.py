a = float(input('Digite 3 medidas para saber se forma um triangulo\nMedida 1: '))
b = float(input('Medida 2: '))
c = float(input('Medida 3: '))
if a < b + c and b < a + c and c < a + b:
    print(f'As medidas {a , b ,  c } formam um triângulo')
else:
    input(f'As medidas {a,b,c}não formam um triangulo')