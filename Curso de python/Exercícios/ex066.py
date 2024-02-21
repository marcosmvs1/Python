#Vários némeros com flags 

n = s = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s = s + n
    c = c + 1

print(f'A soma dos {c} valores foi {s}! ')