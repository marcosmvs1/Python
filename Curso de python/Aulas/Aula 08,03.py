import cpf
num = input('Digite seu cpf: ')
vale = cpf.checar(num)
if vale == True: 
    nome = input('Digite seu nome: ')
    print(f'Olá {nome} seu cpf n:{num} esta válido ')

if vale == False:
    print('Cpf invalido')
