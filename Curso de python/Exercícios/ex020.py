import random
print('VAMOS ORDENAR QUEM APRESENTARÁ O TRABALHO PRIMEIRO')
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
aluno5 = input('Nome do quinto aluno: ')

num = [aluno1, aluno2, aluno3, aluno4, aluno5]

random.shuffle(num)
    
print(f'A ordem de apresentação será: {num}')



