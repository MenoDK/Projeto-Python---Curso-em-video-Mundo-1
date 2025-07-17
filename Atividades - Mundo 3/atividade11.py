num = []
pares = []
impares = []
while True:
    print()
    num.append(int(input('Digite um número: ')))
    print()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print()
        resp = (input('Resposta inválida!\nQuer continuar? [S/N]. '))
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print()
print('-=--=-' * 10)
print()
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
print()