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

#Função title() procupra palavra por palavra e transforoma a priemira letra em maiúscula 
print(frase.title())

#Função strip() ajusta(anula) os espaços do começo e do fim da frase caso exista ex:
frase2 = '   Aprenda python  '
print(frase2.strip())

#função rstrip() ajusta os espaços apenas do fim da frase 
print(frase2.rstrip())

#função lstrip() ajusta os espaços apenas do começo da frase 
print(frase2.lstrip())

#função .split() divide cada palavra da frase em uma lista com todas as palavras de uma cadeia de caracteres
dividido = frase.split()

#função .join() junta as palavras de uma frase separando-as por qualquer caracter desejado, basta colocar o caracter desejado em entre aspas antes do comando .join() ex:
print('-'.join(dividido))

print(dividido.split())

