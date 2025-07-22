num = [[], []]
valor = 0
print('-=--=-' * 10)
print()
for c in range(1, 8):
    valor = int(input(f'Digite o {c} o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print()
print('-=--=-' * 10)
print()
print(f'Os valores digitados foram: {num[0] + num[1]}')
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
print()
print('-=--=-' * 10)
print()