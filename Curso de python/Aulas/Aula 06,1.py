while True:
    entrada_numerica = input('Digite um valor numérico: ')

    if entrada_numerica.isdigit():
        print('Parabéns! Você digitou números corretamente.')
        
        while True:
            nome = input('Agora digite seu nome: ')
            
            if nome.isalpha():
                print('Obrigado, {}!'.format(nome))
                break
            else:
                print('Você precisa digitar apenas letras. Tente novamente.')

        break
    else:
        print('Você precisa digitar números. Tente novamente.')
