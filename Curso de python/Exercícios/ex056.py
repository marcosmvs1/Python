somaidade = 0
mediaidade = 0
maioridadehomenm = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1 , 5):  
    print(f'===== {p} PESSOA ====== ')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: ' ))
    sexo = str(input(f'Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade 
    if p == 1 and sexo in 'Mm':
        maioridadehomenm = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomenm:
        maioridadehomenm = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print(f'A média da idade do grupo é de  {mediaidade} anos')
print(f'O homen mais velho do grupo tem {maioridadehomenm} anos e se chama {nomevelho}')
#print(f'Ao todo são {} mulheres com menos de {} anos')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anosc e se chama ')
                        