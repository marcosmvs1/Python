from datetime import datetime

ano = int(input('Ano de nascimento: '))

idade = datetime.now().year - ano 

if idade < 18:
    print(f'Você inda vai se alistar daqui a \033[0;30;42m {18 - idade } ano(s) \033[m  no ano de \033[0;30;42m {ano + 18} \033[m ')
elif idade == 18:
    print(f'Você esta no ano de alistamento: \033[0;30;43m {(idade )} anos \033[m  ')
elif idade > 18:
    print(f'Você ja passou \033[0;30;41m {idade - 18} anos \033[m da data de alistamento, deveria ter se alistado em \033[0;30;41m {ano + 18} \033[m')
