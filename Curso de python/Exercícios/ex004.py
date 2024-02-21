n = input('digite algo: ')
t =  type(n)
s = n.isspace()
nu = n.isnumeric()
a = n.isalpha()
an = n.isalnum()
mai = n.isupper()
min = n.islower()


print(f'''O tipo primitivo desse valor é: {t}.
Só tem espaços? {s} 
É um número? {nu}
É alfabético? {a}
É alfanúmerico? {an}
É maiúscula? {mai}
É minúscula? {min}''')   
    



