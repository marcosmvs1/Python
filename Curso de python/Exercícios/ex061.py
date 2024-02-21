print('=' * 50)
print('               10 TERMOS DE UMA PA')
print('=' * 50)
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = termo +(11 - 1) * razão
while termo < decimo:
    print(termo)
    termo = termo + razão
print('fim') 

