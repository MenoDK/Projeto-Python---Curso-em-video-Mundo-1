cont = 1
while cont <= 10:
    print(cont, ' --> ', end='')
    cont += 1
print('Acabou')

'''===================================='''
print('==-=='*15)

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')