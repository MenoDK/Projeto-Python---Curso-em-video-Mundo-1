lista = []
for c in range(0, 5):
    print()
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos+1} da lista...')
                break
            pos += 1
print()
print('-=--=-' *10)
print()
print(f'Os valores digitados em ordem foram {lista}')
print()