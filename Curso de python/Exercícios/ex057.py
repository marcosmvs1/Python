sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]

while sexo not in 'FM':
    sexo = str (input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]

if sexo == 'F':
    sexo = 'Feminino'
if sexo == 'M':
    sexo = 'Masculino'
        
    
print(f'Sexo {sexo} resgistrado com sucesso!!! ')