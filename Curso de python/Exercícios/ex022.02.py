nome = str(input('Qual seu nome completo: ')).strip()

print(f'Seu nome com todas as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com todas as letras minusculas é: {nome.lower()}')

separa = nome.split()

print(f'Seu primeiro nome tem {len(separa[0])} letras, o segundo nome tem {len(separa[1])} letras  ')