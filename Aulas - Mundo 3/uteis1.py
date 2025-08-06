if __name__ == "__main__":
    print("Este é o módulo uteis1.")

def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


def linha():
    print()
    print('-=--=-' * 10 )
    print()
