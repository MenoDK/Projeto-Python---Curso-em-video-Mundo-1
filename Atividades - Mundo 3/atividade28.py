from time import sleep

def maior(* núm):
    cont = maior = 0
    print('-=--=-'* 10)
    print()
    print('Analisando os valores... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True )
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}.')
    print()


maior(4, 7, 8, 3, 2, 1)
maior(3, 6, 9)
maior(3, 1)
maior(8)
maior()

print('-=--=-'* 10)
print()