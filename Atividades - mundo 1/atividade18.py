import math 
num = float(input('Digite um número: '))
print(f' O valor digitado foi {num}, sua porção inteira é {math.trunc(num)}')

'''ou '''

from math import trunc
num = float(input('Digite um número: '))
print(f' O valor digitado foi {num}, sua porção inteira é {trunc(num)}')

'''ou '''

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num}, sua porção inteira é {int(num)}')