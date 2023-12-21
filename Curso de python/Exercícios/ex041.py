from datetime import datetime

ano = int(input('Em que ano você nasceu: '))

idade = datetime.now().year - ano

if 0 < idade <= 9:
     print(f'Você tem {idade}anos e sua categoria é a \033[0;30;42m MIRIM \033[m ') 

elif 10 <= idade <= 14:
     print(f'Você tem {idade} anos e sua categoria é a \033[0;30;42m INFANTIL \033[m ') 

elif 15 <= idade <= 19:
     print(f'Você t
           em {idade} anos e sua categoria é a \033[0;30;42m JÚNIOR \033[m ') 

elif 20 <= idade <= 25:
     print(f'Você tem {idade} anos e sua categoria é a \033[0;30;42m SÊNIOR \033[m ') 


elif idade >=26:
     print(f'Você tem {idade} anos e sua categoria é a 03\3[0;30;42m MASTER \033[m ') 


