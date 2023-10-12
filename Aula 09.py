frase= "Curso em Video Python"

#"[:5]"exibe os caracteres conforme o numero foi inserido ex:
print(frase[:3])

#"Len" informa o comprimento da frase ex:
print(len(frase))

#conta a quantidade que a letra solicitada aparece na frase ex:
print(frase.count('o'))

#procura determinda palavra na frase, informando a posição que começa a palavra solicitada ex:
print(frase.find('deo'))

#informa se contem ou não uma palavra em uma frase (True or False )ex:
print('Marcos' in frase)
print('Curso' in frase)

#como substituir uma palavra em um frase 
print(frase.replace('Curso', 'Aula '))

#função upper() trasforma letras minusculas em maiusculas
print(frase.upper())

#função lower() é contrário do upper, transforma as letras maiusculas em minúsculas 
print(frase.lower())

#Função captalize() altera a somente PRIMEIRA letra do texto para maiuscula ex:
print(frase.capitalize())