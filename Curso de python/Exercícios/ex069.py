# PROGRAMA PARA CADASTRO DE PESSOAS 
maior = idade = homens = mulheres = 0 

while True:
    print('-=' *20)
    print('CADASTRE UMA PESSOA ')
    print('-=' *20)
    sexo = ' '
    while sexo not in 'MF':
        idade = int(input('Idade: '))
        sexo = str(input('sexo: [M/F]: ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]): ')).strip().upper()[0]
    if resp == 'N':
        if idade > 18:
            maior = maior + 1
        if sexo == 'M':
            homens = homens + 1
        if sexo == 'F':
            if idade < 20:
                mulheres = mulheres + 1
        break
              

print(f'Total  de pessoas com mais de 18 anos: {maior}')

print(f'Foram cadastrados {homens} homem(s) ')

print(f'Foram cadastradas {mulheres} com menos de 20 anos ')

   

        




    #opção = str(input('Quer continuar: ')).upper() .lower() [0]
    #if opção == 'S':
        


