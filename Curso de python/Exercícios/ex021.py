nome = str(input('Digite seu nome:')).strip()
print(f'Seu nome em maiúscula fica assim: {nome.upper()}')
print(f'Seu nome em minúscula fica assim: {nome.lower()}')
print('Seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')

