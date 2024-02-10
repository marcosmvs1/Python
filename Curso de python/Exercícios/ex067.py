# Programa usar a tabuada, quando o usúario digitar um número abaixo de 0 programa para

while True:
    n = int(input('Quer ver a tabuada de qual valor?: ')) 
    print('-'*30)
    if n < 0:
        break
    else:
        for c in range(1, 11): 
            print(f'{n} X {c} = {n * c} ')
        print('-'*30)
print(f'PROGRAMA TABUADA ENCERRAD0. Volte sempre! ')


