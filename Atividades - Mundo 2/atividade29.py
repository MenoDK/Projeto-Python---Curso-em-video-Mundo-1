print('-'*30)
print('Sequência de Fibonacci ')
print('-'*30)   
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} => {t2}', end='')
cont = 3
mais = 10
while mais != 0:
    while cont <= n:
        t3 = t1 + t2
        print(f' => {t3}', end='')
        t1 = t2
        t2 = t3
        cont += 1
    mais = int(input('\nQuantos termos você quer mostrar a mais?!\n(Digite 0 para finalizar o programa): '))
    n += mais
print(' => FIM')
print('-'*30)