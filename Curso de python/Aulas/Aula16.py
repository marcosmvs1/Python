lanche = 'hambúrger', 'Suco', 'Pizza' , 'Pudim'
print(lanche[1]) # mostra no segundon elemento = 'suco'
print(lanche[3]) # mostra o quarto elemento = 'pudim'
print(lanche[-2]) # mostra do fim para o inicio (no caso 'Pizza')
print(lanche[1:3]) # mostra somente 'Suco' e 'Pudim' pois elimina o elemneto 0 e o elemento 3
print(lanche[2:]) # mostra dop elemento 2 'Pizza' até o fim 'Pudim'
print(lanche[:2]) # mostra do inicio até elemento 2 "Pizza " porém ignora o elemento 2
print(lanche[-2:]) # comessa na 'Pizza' e vai até o ultimo no caso pudim
print(lanche) # mostra toda a tupla 

#PS supla são IMUTAVEIS 

# USABDO FOR 

for c  in lanche:
    print(f'Eu vou comer {c}')
print('To estufado, comi de mais!!')


