print('=' * 50)
print('               10 TERMOS DE UMA PA')
print('=' * 50)
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = termo +(10 - 1) * razão
for c in range(termo, decimo + razão, razão):
    print(f' {c}' , end=' >' ) 
print(' FINISH!!!!')