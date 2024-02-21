a = float(input('Digite 3 medidas para saber se forma um triangulo\nMedida 1: '))
b = float(input('Medida 2: '))
c = float(input('Medida 3: '))

if a <= b + c and b <= a + c and c <=a + b:
    if a and b == c: 
        print(f'As medidas {a , b ,  c } formam um triângulo \033[0;30;42m EQUILÁTERO (todos os lados são iguais) \033[m ')
    
    elif a != b != c != a:
        print(f'As medidas {a , b, c } formamum triângulo \033[0;30;44m ESCALENO (todos os lados diferentes)  \033[m ')  

    else: 
        print(f'As medidas {a , b, c } formamum triângulo \033[0;30;43m ISÓCELES (dois lados iguais e um diferente ) \033[m ') 


else:
    input(f'As medidas {a,b,c}não formam um triangulo')

'''elif a or b == c or c or b == a: 
    print(f'As medidas {a , b, c } formam um triângulo \033[0;30;43m ISÓSELES \033[m ')

elif a != b != c:
    print(f'As medidas {a , b, c } formamum triângulo \033[0;30;44m ESCALENO \033[m ')  

if a < b + c and b < a + c and c < a + b:
    print(f'As medidas {a , b ,  c } formam um triângulo')
else:
    input(f'As medidas {a,b,c}não formam um triangulo')'''  