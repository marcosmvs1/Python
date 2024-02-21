nome = str (input("Digite seu nome: "))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[4:33m',
         'pretoebranco': '\033[7m'}
print(f"Olá! Muito prazer em te conhecer {cores['amarelo']}{nome}\033[m!!!")