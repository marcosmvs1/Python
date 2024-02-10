
#Interronpendo repetições WHILE usando BREAk
n = s = 0
while True:
    n = int(input('Digite um número: ')) 

#No caso a Função 'BREAK' é usada como comando de parada para um ciclo executado em while (assim que for digitado o comanto '999' o sistema para a sequência )
    
    if n == 999:
        break
    s += n
print(f'A soma vale: {s}')

