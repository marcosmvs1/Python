from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}° pessoa: '))
    if date.today().year - ano >= 21:  
        maior += 1
    else:
        menor += 1

print(f'Das {c} Pessoas {menor} tem menos de 21 anos e {maior} Pessoas são maiores de 21 anos  ')
