peso = float (input('Qual é seu peso: '))
altura = float(input('Qual sua altura: '))
imc = peso / (altura ** 2)

if imc < 17:
    print(f'IMC = \033[0;30;42m {imc} \033[m  Muito abaixo do peso ideal')

elif 17 < imc < 18.49:
    print(f'IMC = \033[0;30;43m {imc} \033[m Abaixo do peso ideal')

elif 18.5 < imc < 24.99:
    print(f'IMC = \033[0;30;44m {imc} \033[m Peso ideal')

elif 25 < imc < 29.99:
    print(f'IMC = \033[0;30;45m {imc} \033[m Acima do peso ideal')

elif 30 < imc < 34.99:
    print(f'IMC = \033[0;30;46m {imc} \033[m Obesidade grau 1')