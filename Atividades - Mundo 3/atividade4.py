num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('-=-=' * 10)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes ')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição ')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print( n, end=' ')