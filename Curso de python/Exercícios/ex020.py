import random
print('VAMOS ESCOLHER UM ALUNO PARA APAGAR O QUADRO')
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
aluno5 = input('Nome do quinto aluno: ')

num = [aluno1, aluno2, aluno3, aluno4, aluno5]

alunos = random.choice(num)

print(f'O alunmo escolhido para apagar o quadro foi {alunos}')















'''import random

# Lista de nomes dos alunos
alunos = ["João", "Maria", "Pedro", "Ana"]

# Escolhendo um aluno aleatoriamente
aluno_escolhido = random.choice(alunos)

# Mostrando o nome do aluno escolhido
print(f"O aluno escolhido para apagar o quadro é: {aluno_escolhido}")'''