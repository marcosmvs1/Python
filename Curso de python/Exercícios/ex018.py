from math import sin, cos, tan, radians
ang = float (input('Qual ângulo: '))

print(f'O ãngulo de {ang} tem o SENO de {sin(radians(ang)):.2F}')
print(f'O ângulo de {ang} tem o COSSENO de {cos(radians(ang)):.2F}')
print(f'O ângulo de {ang} tem a tangente de {tan(radians(ang)):.2F}')