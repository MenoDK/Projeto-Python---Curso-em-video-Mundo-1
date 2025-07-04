lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida} ')
print('Comi para caramba! ')

print('=-=-='*10)

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi para caramba! ')

print('=-=-='*10)

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos} ')
print('Comi para caramba! ')

print('=-=-='*10)

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi para caramba! ')

print('=-=-='*10)

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))
print(lanche)
