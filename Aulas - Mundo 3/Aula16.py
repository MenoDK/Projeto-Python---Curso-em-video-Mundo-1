print('-=--=-' * 10)
print('EX9')
print()

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b 
print(s)


print()
print('-=--=-' * 10)


print('EX10')
print()

def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)


print()
print('-=--=-' * 10)


print('EX11')
print()

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é igual {s}')


soma(4, 5)
soma(b = 8, a = 9)
soma(2, 1)


print()
print('-=--=-' * 10)


print('EX12')
print()

def soma(* valores):
    s = 0 
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4) 

print()