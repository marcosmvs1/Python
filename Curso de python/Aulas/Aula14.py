'''c = 1
while c < 10:
    print(c) 
    c = c + 1
print('FIM!!!')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        if n % 2 != 0:
            impar += 1
print(f'você digitou {par} números pares e {impar} números impares ') 