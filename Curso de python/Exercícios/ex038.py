n1 =  int(input('Primeiro número: '))
n2 =  int(input('Segundo número: '))

if n1 > n2:
    print('\033[0;30;42m O PRIMEIRO \033[m  valor é maior ')
elif n2 > n1:
    print('\033[0;30;41m O SEGUNDO \033[m número é maior ')

elif n1 == n2:
    print('\033[0;30;43m OS DOIS \033[m núnmeros são iguais ') 