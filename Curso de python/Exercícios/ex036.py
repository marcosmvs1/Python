casa = float(input('Qual valor da casa: '))
salario = float(input('Qual seu salário: '))
anos = int(input('Quantos anos: '))

por = (salario * 30) / 100 # Porcentagem do salário 
parcelas = casa /  (anos * 12) # Qtde de mêses  

if parcelas <= por:
    print(f'A porcentagem é {por}\nAs parcelas ficam em {parcelas:.2F}\nSeu financiamento foi APROVADO!!')
else:
    print(f'A porcentagem é {por}\nAs parcelas ficam em {parcelas}\nSeu financiamento foi REPROVADO!!')