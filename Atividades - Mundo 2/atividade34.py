while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n == 0:
        break
    for c in range (1,11):
        print(f'{n} X {c} = {n*c} ')
    print('-' *30)
    print('DIGITE 0 PARA TERMINAR O PROGRAMA ')
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE ')