print('-=--=-' * 10)
print('EX1')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'lista A {a}')
print(f'lista B {b}')
print()

print('-=--=-' * 10)
print('EX2')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'lista A {a}')
print(f'lista B {b}')
print()