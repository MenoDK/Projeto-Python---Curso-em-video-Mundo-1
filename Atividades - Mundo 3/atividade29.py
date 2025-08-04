from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='' , flush=True)
        sleep(0.3)
    print('Pronto')


def SomaPar(lista):
    soma = 0
    pares = []
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            pares.append(valor)
    print(f'Os valores pares são {pares}')
    print(f'Somando valores pares de {lista}, temos {soma}')


def linha():
    print()
    print('-=--=-' *10)
    print()


numeros = list()

linha()
sorteia(numeros)
linha()
SomaPar(numeros)
linha()