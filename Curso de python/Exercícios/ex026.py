frase = str(input('Digite uma fraase: ')).upper().strip()
vezes = frase.count('A')
pri = frase.find('A') + 1
ult = frase.rfind('A')
print(f'A letra A aparece na frase {vezes} vezes')
print(f'A primeira letra A esta na posição: {pri}')
print(f'A última  letra A esta na posição: {ult}')
