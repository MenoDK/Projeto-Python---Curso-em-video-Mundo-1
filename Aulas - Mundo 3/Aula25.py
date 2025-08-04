def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()


linha()
print('Ex23:')
print()

n = int(input('Digite um nùmero: '))
print()
print(f'O fatorial de {n} é igual a {fatorial(n)} ')


linha()
print('Ex24:')
print()

f1 = fatorial (5)
f2 = fatorial (4)
f3 = fatorial ()

print(f'Os resultados são: \n fatorial (5) = {f1}\n fatorial (4) = {f2}\n fatorial () = {f3}')

linha()
