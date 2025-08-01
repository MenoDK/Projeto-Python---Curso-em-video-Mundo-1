print('-=--=-' * 10)
print('EX13')
print()
def contador(* num):
    print(num)


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)


print()
print('-=--=-' * 10)


print('EX14')
print()

def contador(* num):
    for valor in num:
        print(f'{valor}',end=' ')
    print('FIM')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)


print()
print('-=--=-' * 10)


print('EX15')
print()

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)


print()

