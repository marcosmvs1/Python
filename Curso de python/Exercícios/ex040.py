nota1 = float(input('Qual é a nota da primeira prova: '))
nota2 = float(input('Qual é a nota da sugunda prova: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média foi \033[0;30;41m {media} \033[m \033[0;30;41m VOCÊ FOI REPROVADO \033[m ') 

elif  7 > media >= 5:
    print(f'Sua média foi \033[0;30;43m {media} \033[m  \033[0;30;43m  VOCÊ ESTÁ DE RECUPERAÇÃO \033[m ') 

elif media >= 7:
    print('Parabéns \033[0;30;42m VOCÊ FOI APROVADO \033[m ')