print('-=--=-' * 10)
print('EX1')
print()

galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    print()
    dado.clear()
print(galera)
print()

print('-=--=-' * 10)
print('EX2')
print()

galera2= []
dado2 = []
totmai = totmen = 0
for c in range(0, 3):
    dado2.append(str(input('Nome: ')).strip())
    dado2.append(int(input('Idade: ')))
    galera2.append(dado2[:])
    print()
    dado2.clear()
for p in galera2:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
        print()
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
        print()
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
print()
