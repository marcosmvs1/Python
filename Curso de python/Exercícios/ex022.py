nome = str(input('Qual seu nome completo: ')).strip()

print(f'Seu nome com todas as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com todas as letras minusculas é: {nome.lower()}')
letras = len(nome) - nome.count(' ')
print(f'Seu nome tem {letras} letras ')
pl = nome.find(' ')
print(f'Seu primeiro nome tem {pl} letras ')