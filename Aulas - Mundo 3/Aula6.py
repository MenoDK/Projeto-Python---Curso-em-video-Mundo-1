print('EX1')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print()
for v in valores:
    print(f'{v}...', end='')
print()

print('-=--=-'*10)
print('EX2')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print()
    print(f'Na posição {c} encontrei o valor {v}!')
print()

print('-=--=-'*10)
print('EX3')
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
print()
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
    print()