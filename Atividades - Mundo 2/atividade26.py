from math import factorial
na = int(input('Digite um número para calcular seu fatorial: '))
fa = factorial(na)
print(f'O fatorial de {na} é {fa}')

'''ou '''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n 
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')