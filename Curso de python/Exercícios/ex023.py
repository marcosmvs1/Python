num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'''Ánalisando o número {num}
A unidade é: {u}
A dezena é: {d}
A centena é: {c}
A milher é: {m}''')