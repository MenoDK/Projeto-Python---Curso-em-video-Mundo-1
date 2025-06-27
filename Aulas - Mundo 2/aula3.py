n = int(input('Digite um numéro: '))
for c in range(0, n+1):
    print(c)
print('Fim')

print('-=-'*15)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

print('-=-'*15)

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')

print('-=-'*15)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')