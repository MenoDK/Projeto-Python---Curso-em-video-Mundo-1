from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-' * 30)
print()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('-=' * 3, f'sorteando {quant} jogos', '-=' * 3)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
print()