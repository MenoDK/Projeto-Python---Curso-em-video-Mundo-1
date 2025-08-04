def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale: {a} ')
    print(f'A dentro vale: {b} ')
    print(f'A dentro vale: {c} ')


def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()


a = 5
linha()

teste(a)
linha()

print(f'A fora vale: {a} ')
linha()