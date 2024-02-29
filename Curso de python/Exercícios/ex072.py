num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze' , 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

digi = int(input('Digite um número entre 0 e 20: '))
opcao = 'S'
while digi < 0 or digi >= 21 and opcao == 'S':
    digi = int(input('tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {num[digi]}')

opcao = str(input('Você quer continuar? S/N ')) . strip() .upper() [0]   

print('fim')

    



        
    





